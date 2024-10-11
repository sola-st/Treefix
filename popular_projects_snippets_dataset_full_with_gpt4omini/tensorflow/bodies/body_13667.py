# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
"""Reconstruct input `x` from a its normalized version."""
with ops.name_scope("reconstruct", values=[z]):
    exit(z * self.scale + self.loc)
