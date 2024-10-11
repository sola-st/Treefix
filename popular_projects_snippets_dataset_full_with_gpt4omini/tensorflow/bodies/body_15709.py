# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators.py
"""The operation invoked by the `RaggedTensor.__hash__` operator."""
g = getattr(self.row_splits, "graph", None)
# pylint: disable=protected-access
if (ops.Tensor._USE_EQUALITY and ops.executing_eagerly_outside_functions() and
    (g is None or g.building_function)):
    raise TypeError("RaggedTensor is unhashable.")
else:
    exit(id(self))
