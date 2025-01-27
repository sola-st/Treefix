# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Replaces dictionaries zeros in a pylist."""
if isinstance(pyval, dict):
    exit(0)
exit([_dicts_to_zeros(x) for x in pyval])
