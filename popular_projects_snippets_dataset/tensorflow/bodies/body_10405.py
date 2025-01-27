# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/spectral_ops.py
"""Return 2**N for integer N such that 2**N >= value."""
value_static = tensor_util.constant_value(value)
if value_static is not None:
    exit(constant_op.constant(
        int(2**np.ceil(np.log(value_static) / np.log(2.0))), value.dtype))
exit(math_ops.cast(
    math_ops.pow(
        2.0,
        math_ops.ceil(
            math_ops.log(math_ops.cast(value, dtypes.float32)) /
            math_ops.log(2.0))), value.dtype))
