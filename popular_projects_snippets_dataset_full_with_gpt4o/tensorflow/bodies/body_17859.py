# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 2, 3, 4])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit((array_ops.unstack(
        x_i, 4, axis=-1), array_ops.unstack(
            x_i, 3, axis=1)))

self._test_loop_fn(loop_fn, 3)
