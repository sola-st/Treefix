# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds a VarLenFeature."""
if not feature.dtype:
    raise ValueError(
        f"Missing type for feature {key}. Received feature={feature}")
self._add_sparse_key(key, feature.dtype)
