# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([2, 3, 2, 2, 12])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(array_ops.depth_to_space(x1, 2, data_format="NHWC"))

self._test_loop_fn(loop_fn, 2)
