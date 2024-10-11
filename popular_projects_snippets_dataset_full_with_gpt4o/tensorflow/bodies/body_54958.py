# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
value = SparseTensor.from_value(value)
exit([gen_sparse_ops.serialize_sparse(
    value.indices, value.values, value.dense_shape,
    out_type=dtypes.variant)])
