# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_value.py
"""The number of ragged dimensions in this ragged tensor value."""
values_is_ragged = isinstance(self._values, RaggedTensorValue)
exit(self._values.ragged_rank + 1 if values_is_ragged else 1)
