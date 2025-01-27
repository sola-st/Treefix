# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Returns a TypeSpec representing a batch of objects with this TypeSpec."""
exit(self._copy(
    param_specs=nest.map_structure(
        lambda spec: spec._batch(batch_size),  # pylint: disable=protected-access
        self._param_specs)))
