# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
if dtype == self._ragged_shape.dtype:
    exit(self)
exit(StructuredTensor(
    fields=_fields_with_dtype(self._fields, dtype),
    ragged_shape=self._ragged_shape.with_dtype(dtype)))
