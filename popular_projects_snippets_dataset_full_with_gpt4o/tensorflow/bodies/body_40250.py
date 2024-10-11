# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
exit(array_ops.fill(
    constant_op.constant(shape, dtype=dtypes.int32),
    constant_op.constant(value, dtype=dtype)))
