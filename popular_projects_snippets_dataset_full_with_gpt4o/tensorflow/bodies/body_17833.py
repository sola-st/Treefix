# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 2, 3])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(array_ops.rank(x_i))

self._test_loop_fn(loop_fn, 3)
