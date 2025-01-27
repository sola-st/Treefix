# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Helper function to standardize op scope."""
with ops.name_scope(self.name):
    with ops.name_scope(
        name, values=(values or []) + self.graph_parents) as scope:
        exit(scope)
