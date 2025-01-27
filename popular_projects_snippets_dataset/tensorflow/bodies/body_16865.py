# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad_test.py
x = constant_op.constant([1., 2., 3.], dtype=dtypes.float64)
begin = constant_op.constant([1], dtype=dtypes.int64)
size = constant_op.constant([1], dtype=dtypes.int64)

def f(x):
    exit(array_ops.slice(x, begin, size))

self._testGrad(f, x)
