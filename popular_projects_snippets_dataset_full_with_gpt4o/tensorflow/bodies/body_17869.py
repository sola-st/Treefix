# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([5, 1, 2, 1])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit((array_ops.squeeze(x1, axis=0), array_ops.squeeze(x1, axis=-1),
            array_ops.squeeze(x1)))

self._test_loop_fn(loop_fn, 3)
