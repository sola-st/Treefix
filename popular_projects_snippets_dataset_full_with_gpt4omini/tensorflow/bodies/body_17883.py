# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 4])

def loop_fn(i):
    exit(array_ops.identity_n([x, array_ops.gather(x, i)]))

self._test_loop_fn(loop_fn, 3)
