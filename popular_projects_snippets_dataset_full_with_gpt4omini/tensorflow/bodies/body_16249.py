# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if self._flat_values_spec is not None:
    raise ValueError("Customized value_type is not supported.")
result = RaggedTensor._from_variant(  # pylint: disable=protected-access
    tensor_list[0],
    dtype=self._dtype,
    row_splits_dtype=self._row_splits_dtype,
    output_ragged_rank=self._ragged_rank)
if self._shape.ndims is not None:
    if isinstance(result, RaggedTensor):
        result._set_shape(self._shape)  # pylint: disable=protected-access
        # TODO(xjun): MaskedTensor doesn't implement set_shape.
        if self.flat_values_spec is not None and hasattr(self.flat_values,
                                                         "set_shape"):
            result.flat_values.set_shape(self.flat_values_spec.shape)
    else:
        result.set_shape(self._shape)
exit(result)
