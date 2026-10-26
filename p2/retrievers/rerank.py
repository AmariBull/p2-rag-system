"""Reranking (stage 1): Claude reorders a first-stage system's top 20.

It is the 13 lab's rerank_one() from pipeline.py:
- the first stage's top 20 go to Claude as numbered passages, each cut to its first 600 characters;
- the schema forces the reply into {"order": [20 numbers]}, each from 1 to 20, and a reply that is
  not each number once keeps the first-stage order (with a warning), so a bad call is visible;
- the documents below the 20 keep their first-stage order underneath.

The first stage, the number of candidates and the passage length come from [rerank] in p2.toml
(hybrid, 20 and 600 by default). Every call goes through p2.claude.call, which caches replies and
records the tokens in the run's trace. search_chunks does the same over the first stage's top chunks,
for `p2 answer`.

Scores: the reranked candidates get 2 - position / candidates (2.00, 1.95, ... 1.05 for 20), which
sits above every first-stage score below them (RRF scores are under 0.04), so the file stays in order.
"""

from __future__ import annotations

import sys

from p2 import claude, retrievers

NEEDS_CLAUDE = True

PROMPT = """Below are {n} passages from a document collection, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n):
    numbers = {"type": "integer", "minimum": 1, "maximum": n}
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": numbers, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        settings = cfg.table("rerank")
        self.cfg = cfg
        self.first_name = settings.get("first_stage", "hybrid")
        self.candidates = settings.get("candidates", 20)
        self.passage_chars = settings.get("passage_chars", 600)
        self.first = retrievers.build(self.first_name, corpus, cfg)
        self.model = cfg.model
        self.doc_text = {docid: doc.text for docid, doc in corpus.docs.items()}
        self.chunk_text = corpus.chunk_texts(cfg.chunk_words, cfg.chunk_overlap)

    def rerank(self, text, ranked, texts):
        """ranked: [(id, score), ...] from the first stage; returns the same ids, top candidates reordered."""
        top, rest = ranked[: self.candidates], ranked[self.candidates :]
        n = len(top)
        if n < 2:
            return ranked
        passages = "\n\n".join(f"[{i}] {texts[item][: self.passage_chars]}" for i, (item, _) in enumerate(top, 1))
        prompt = PROMPT.format(n=n, query=text, passages=passages)
        reply = claude.call(prompt, schema(n), model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg))
        order = (reply.output or {}).get("order")
        if reply.error or not isinstance(order, list) or sorted(order) != list(range(1, n + 1)):
            problem = reply.error or f"reply was not each of 1 to {n} once: {order}"
            print(f"WARNING: {problem}; kept the {self.first_name} order for {text[:60]!r}", file=sys.stderr)
            order = list(range(1, n + 1))
        reranked = [(top[i - 1][0], 2 - pos / n) for pos, i in enumerate(order)]
        return reranked + rest

    def search(self, text, k):
        ranked = self.first.search(text, max(k, self.candidates))
        return self.rerank(text, ranked, self.doc_text)[:k]

    def search_chunks(self, text, k):
        ranked = self.first.search_chunks(text, max(k, self.candidates))
        return self.rerank(text, ranked, self.chunk_text)[:k]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
