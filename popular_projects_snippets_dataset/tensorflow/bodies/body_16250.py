# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if self._flat_values_spec is not None:
    raise ValueError("Customized value_type is not supported.")
exit(RaggedTensorSpec(
    tensor_shape.TensorShape([batch_size]).concatenate(self._shape),
    self._dtype, self._ragged_rank + 1, self._row_splits_dtype))
