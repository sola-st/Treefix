# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 2, 3])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit((array_ops.shape(x_i), array_ops.shape(x_i, out_type=dtypes.int64)))

self._test_loop_fn(loop_fn, 3)
