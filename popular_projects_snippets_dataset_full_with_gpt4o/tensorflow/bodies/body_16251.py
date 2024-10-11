# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if self._flat_values_spec is not None:
    raise ValueError("Customized value_type is not supported.")
# Note: Negative ragged_rank is allowed here because the dataset could be
# subsequently batched again. If ragged_rank > 1, assume row_splits_dtype is
# consistent. Errors are handled in
# RaggedTensorSpec._from_compatible_tensor_list()
exit(RaggedTensorSpec(self._shape[1:], self._dtype, self._ragged_rank - 1,
                        self._row_splits_dtype))
