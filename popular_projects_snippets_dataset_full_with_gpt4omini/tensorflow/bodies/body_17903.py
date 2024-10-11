# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([2, 3, 12, 12, 3])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(array_ops.space_to_depth(x1, 2, data_format="NHWC"))

self._test_loop_fn(loop_fn, 2)
