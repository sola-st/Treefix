# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
exit(array_ops.placeholder_with_default(
    constant_op.constant(v, dtype=dtypes.int64),
    tensor_shape.TensorShape(None)))
