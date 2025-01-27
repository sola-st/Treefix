# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 6, 3])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit((array_ops.split(x1, [2, 1, 3],
                            axis=0), array_ops.split(x1, [3], axis=-1)))

self._test_loop_fn(loop_fn, 3)
