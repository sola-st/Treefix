# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([4, 2, 3])
y = random_ops.random_uniform([4, 2, 3])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    y_i = array_ops.gather(y, i)
    x_0 = array_ops.gather(x, 0)
    exit((math_ops.cross(x_i, y_i), math_ops.cross(x_0, y_i)))

self._test_loop_fn(loop_fn, 4)
