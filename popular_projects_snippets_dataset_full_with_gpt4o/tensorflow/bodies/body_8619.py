# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with backprop.GradientTape() as tape:
    x = array_ops.ones([5, 5])
    tape.watch(x)
    y = math_ops.reduce_euclidean_norm(x, axis=constant_op.constant(1))
exit((y, tape.gradient(y, x)))
