# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
result = tensor_list[0]
if (all(isinstance(t, np.ndarray) for t in tensor_list) and
    not tf2.enabled()):
    for row_splits in reversed(tensor_list[1:]):
        result = ragged_tensor_value.RaggedTensorValue(result, row_splits)
else:
    if isinstance(tensor_list[0], np.ndarray):
        tensor_list = [ops.convert_to_tensor(t) for t in tensor_list]
        result = tensor_list[0]
    for row_splits in reversed(tensor_list[1:]):
        result = RaggedTensor(
            result,
            RowPartition.from_row_splits(row_splits, validate=False),
            internal=True)
if self._shape.ndims is not None:
    if isinstance(result, RaggedTensor):
        result._set_shape(self._shape)  # pylint: disable=protected-access
        # TODO(xjun): MaskedTensor doesn't implement set_shape.
        if self.flat_values_spec is not None and hasattr(result.flat_values,
                                                         "set_shape"):
            result.flat_values.set_shape(self.flat_values_spec.shape)
    elif isinstance(result, ops.Tensor):
        result.set_shape(self._shape)
exit(result)
