# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 2, 3])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    z = array_ops.zeros_like(x1),
    exit((z, z + x1))

self._test_loop_fn(loop_fn, 3)
