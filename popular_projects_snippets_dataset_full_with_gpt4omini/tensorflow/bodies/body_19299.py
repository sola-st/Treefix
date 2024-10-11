# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateless_random_ops.py
exit(bitwise_ops.bitwise_or(
    math_ops.cast(x[0], dtypes.uint64),
    bitwise_ops.left_shift(math_ops.cast(x[1], dtypes.uint64),
                           constant_op.constant(32, dtypes.uint64))))
