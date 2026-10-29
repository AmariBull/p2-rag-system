"""Ablation of dense: the same model and query prefix, with 150-word chunks instead of 300.

The only change is chunk_words (the overlap stays at p2.toml's 50 words), made on a copy of
the settings so p2.toml, which every system shares, is untouched.
"""

from __future__ import annotations

from p2.retrievers.dense import Dense

BASE = "dense"
NEEDS_CLAUDE = False


def build(corpus, cfg):
    return Dense(corpus, cfg.replace(chunk_words=150))
