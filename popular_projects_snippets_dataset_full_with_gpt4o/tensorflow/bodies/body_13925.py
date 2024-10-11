# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Helper function to standardize op scope."""
with ops.name_scope(self.name):
    with ops.name_scope(name, values=(
        ([] if values is None else values) + self._graph_parents)) as scope:
        exit(scope)
