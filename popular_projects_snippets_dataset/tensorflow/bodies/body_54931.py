# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Creates a `SparseTensor`.

    Args:
      indices: A 2-D int64 tensor of shape `[N, ndims]`.
      values: A 1-D tensor of any type and shape `[N]`.
      dense_shape: A 1-D int64 tensor of shape `[ndims]`.

    Raises:
      ValueError: When building an eager SparseTensor if `dense_shape` is
        unknown or contains unknown elements (None or -1).
    """
with ops.name_scope(None, "SparseTensor", [indices, values, dense_shape]):
    indices = ops.convert_to_tensor(
        indices, name="indices", dtype=dtypes.int64)
    # TODO(touts): Consider adding mutable_values() when 'values'
    # is a VariableOp and updating users of SparseTensor.
    values = ops.convert_to_tensor(values, name="values")

    dense_shape = ops.convert_to_tensor(
        dense_shape, name="dense_shape", dtype=dtypes.int64)
    dense_shape_default = tensor_util.constant_value_as_shape(dense_shape)

self._indices = indices
self._values = values
self._dense_shape = dense_shape
self._dense_shape_default = dense_shape_default

indices_shape = indices.shape.with_rank(2)
values_shape = values.shape.with_rank(1)
dense_shape_shape = dense_shape.shape.with_rank(1)

# Assert number of rows in indices match the number of elements in values.
indices_shape.dims[0].assert_is_compatible_with(values_shape.dims[0])
# Assert number of columns in indices matches the number of elements in
# dense_shape.
indices_shape.dims[1].assert_is_compatible_with(dense_shape_shape.dims[0])
