# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([2, 3, 4])

def loop_fn(i):
    a = array_ops.gather(x, i)
    exit(math_ops.bucketize(a, [-1, 0.5, 1]))

self._test_loop_fn(loop_fn, 2)
