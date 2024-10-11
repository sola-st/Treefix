# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py

def func(x):
    y = x * constant_op.constant([[1.], [3.]])
    y = y.with_values(array_ops.stop_gradient(y.values))
    z = x * y
    exit(math_ops.reduce_sum(z))

self._testGradient(func, [[1., 2.], [3., 4., 5.]],
                   [[1., 2.], [9., 12., 15.]])
