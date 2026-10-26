"""Hybrid retrieval (stage 1): reciprocal rank fusion (RRF) of two systems' rankings.

It is the 13 lab's rrf() from pipeline.py: each document scores the sum of 1 / (k + rank) over the
rankings, with k = 60 and rank counted from 1. Only ranks matter, so bm25's scores (0 to ~20) and
dense's cosine similarities (-1 to 1) never need to be put on one scale.

The two systems and k come from [hybrid] in p2.toml (bm25 and dense, k 60, by default). Each is
built through p2.retrievers.build, so a run of several systems builds each index once, and each is
asked for its full ranking, because a document 11th in both lists can belong in the fused top 10.
search_chunks fuses the two chunk rankings the same way, for `p2 answer`.
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False


def rrf(rankings, k):
    """[(id, score), ...] lists, best first -> fused (id, score) pairs, best first, ties in id order."""
    fused: dict[str, float] = {}
    for ranking in rankings:
        for rank, (item, _) in enumerate(ranking, 1):
            fused[item] = fused.get(item, 0.0) + 1 / (k + rank)
    return order(fused.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        settings = cfg.table("hybrid")
        self.names = settings.get("systems", ["bm25", "dense"])
        self.k = settings.get("k", 60)
        self.systems = [retrievers.build(name, corpus, cfg) for name in self.names]
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(corpus.chunks(cfg.chunk_words, cfg.chunk_overlap))
        self.model = next((getattr(s, "model", None) for s in self.systems if getattr(s, "model", None)), None)

    def search(self, text, k):
        return rrf([s.search(text, self.n_docs) for s in self.systems], self.k)[:k]

    def search_chunks(self, text, k):
        return rrf([s.search_chunks(text, self.n_chunks) for s in self.systems], self.k)[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
