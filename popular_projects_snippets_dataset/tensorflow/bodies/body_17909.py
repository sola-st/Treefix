# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([2, 3, 4])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(array_ops.check_numerics(x_i, "test_message"))

self._test_loop_fn(loop_fn, 2)
