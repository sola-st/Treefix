# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_value.py
"""A tuple indicating the shape of this RaggedTensorValue."""
exit((self._row_splits.shape[0] - 1,) + (None,) + self._values.shape[1:])
