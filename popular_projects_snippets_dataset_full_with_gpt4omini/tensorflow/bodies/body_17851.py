# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 2, 5, 3])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(array_ops.slice(x1, begin=(0, 2 - i, i), size=(-1, 2, 1)))

self._test_loop_fn(loop_fn, 3)
