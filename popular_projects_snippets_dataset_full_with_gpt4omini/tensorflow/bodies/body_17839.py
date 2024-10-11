# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py

def loop_fn(i):
    exit(array_ops.fill((2, 3), i))

self._test_loop_fn(loop_fn, 3)
