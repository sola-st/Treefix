# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Helper function to standardize op scope."""
full_name = self.name
if name is not None:
    full_name += "/" + name
with ops.name_scope(full_name) as scope:
    exit(scope)
