# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([3, 6, 7])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(array_ops.ensure_shape(x_i, [6, 7]))

self._test_loop_fn(loop_fn, 3)
