# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([3, 5])
y = random_ops.random_uniform([3, 5])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    y1 = array_ops.gather(y, i)
    exit(math_ops.approximate_equal(x1, y1))

self._test_loop_fn(loop_fn, 3)
