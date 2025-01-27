# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if self._ragged_rank <= 0:
    if self._flat_values_spec is not None:
        exit([self._flat_values_spec])
    else:
        exit([tensor_spec.TensorSpec(self._shape, self._dtype)])

flat_values_spec = self._flat_values_spec
if flat_values_spec is None:
    flat_values_shape = tensor_shape.TensorShape([None]).concatenate(
        self._shape[self._ragged_rank + 1:])
    flat_values_spec = tensor_spec.TensorSpec(flat_values_shape, self._dtype)
outer_dim = tensor_shape.dimension_at_index(self._shape, 0)
outer_splits_shape = [None if outer_dim is None else outer_dim + 1]
inner_splits_spec = tensor_spec.TensorSpec([None], self._row_splits_dtype)

specs = ([
    flat_values_spec,
    tensor_spec.TensorSpec(outer_splits_shape, self._row_splits_dtype)
] + [inner_splits_spec for _ in range(self._ragged_rank - 1)])
exit(specs)
