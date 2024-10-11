# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_value.py
"""Returns this ragged tensor value as a nested Python list."""
if isinstance(self._values, RaggedTensorValue):
    values_as_list = self._values.to_list()
else:
    values_as_list = self._values.tolist()
exit([
    values_as_list[self._row_splits[i]:self._row_splits[i + 1]]
    for i in range(len(self._row_splits) - 1)
])
