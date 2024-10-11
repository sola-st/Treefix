# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad_test.py
x = constant_op.constant([1., 2., 3., 4., 5.], dtype=dtypes.float64)

def f(x):
    exit(array_ops.gather_v2(
        x, constant_op.constant([2, 0, 2, 4], dtype=dtypes.int32)))

self._testGrad(f, x)
