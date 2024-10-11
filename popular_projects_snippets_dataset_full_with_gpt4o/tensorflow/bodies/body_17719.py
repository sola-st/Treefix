# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a = constant_op.constant(3.)
x = random_ops.random_uniform([4, 5])
y = random_ops.random_uniform([6, 5])
n = x.shape[0]

def loop_fn(i):
    exit(math_ops.tanh(a * array_ops.gather(x, i) + array_ops.gather(y, i)))

self._test_loop_fn(loop_fn, n)
