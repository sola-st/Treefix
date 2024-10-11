# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
"""Standardize input `x` to a unit normal."""
with ops.name_scope("standardize", values=[x]):
    exit((x - self.loc) / self.scale)
