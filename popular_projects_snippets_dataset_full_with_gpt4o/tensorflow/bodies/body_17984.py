# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([5, 5, 6])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(manip_ops.roll(x_i, i, axis=0))

self._test_loop_fn(loop_fn, 5)
