# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad_test.py
x = constant_op.constant([1., 2., 3.], dtype=dtypes.float64)
y = constant_op.constant([2, 3], dtype=dtypes.int64)

def f(x):
    exit(array_ops.broadcast_to(
        x,
        y))

self._testGrad(f, x)
