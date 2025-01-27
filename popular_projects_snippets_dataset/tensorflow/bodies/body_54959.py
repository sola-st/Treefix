# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
dense_shape = tensor_util.constant_value_as_shape(value.dense_shape)
if self._shape.merge_with(dense_shape).ndims == 0:
    raise ValueError(
        "Unbatching a sparse tensor is only supported for rank >= 1. "
        f"Obtained input: {value}.")
exit([gen_sparse_ops.serialize_many_sparse(
    value.indices, value.values, value.dense_shape,
    out_type=dtypes.variant)])
