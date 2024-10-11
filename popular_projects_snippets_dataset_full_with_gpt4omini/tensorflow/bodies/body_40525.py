# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = array_ops.ones([2, 4, 2])
length = constant_op.constant([2, 3, 4, 4], dtype=dtypes.int64)
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = array_ops.repeat(x, [2], axis=1)
    y = y[:, :math_ops.reduce_max(length), :]
tape.batch_jacobian(y, x)
