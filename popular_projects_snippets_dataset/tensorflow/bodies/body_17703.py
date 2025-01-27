# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([2, 3, 4])

def loop_fn(i):
    a = array_ops.gather(x, i)
    exit(clip_ops.clip_by_value(a, 0.5, 1.0))

self._test_loop_fn(loop_fn, 2)
