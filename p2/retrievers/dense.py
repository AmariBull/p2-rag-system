"""Dense retrieval (stage 1): embed every chunk once, embed the query, and rank chunks by cosine similarity.

It is the embedding arm of the 12 lab's retrieve.py (dense_rankings) moved onto chunks:
- the model comes from [dense] model in p2.toml (bge-small-en-v1.5 by default);
- chunk vectors come from p2/embed.py's doc_vectors, cached in .cache/vectors/, so only the
  first run encodes the corpus;
- every vector has length 1, so one matrix-vector product gives each chunk's cosine similarity.

[dense] query_prefix is put in front of each query before it is embedded ("" by default); the
bge-small model card recommends an instruction there, which the 12 lab's stretch measured.
"""

from __future__ import annotations

import numpy as np

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        settings = cfg.table("dense")
        self.model = settings.get("model", embed.BGE)
        self.prefix = settings.get("query_prefix", "")
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> np.ndarray:
        if not len(self.chunks):
            return np.zeros(0, dtype=np.float32)
        query = self.embedder.encode([self.prefix + text])[0]
        return self.vectors @ query


def build(corpus, cfg):
    return Dense(corpus, cfg)
