# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
as_zeros = [
    zeros_like_v2(value, dtype=dtypes.int32) for value in values
]
result = leaf_op(as_zeros)
exit(_structured_tensor_like(result))
