# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds a sparse key & dtype, checking for duplicates."""
if key in self.sparse_keys:
    original_dtype = self.sparse_types[self.sparse_keys.index(key)]
    if original_dtype != dtype:
        raise ValueError(
            f"Conflicting type {original_dtype} vs {dtype} for feature {key}.")
else:
    self.sparse_keys.append(key)
    self.sparse_types.append(dtype)
