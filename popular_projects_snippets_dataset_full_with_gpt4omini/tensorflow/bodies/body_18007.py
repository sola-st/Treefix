# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(_):
    exit(random_ops.random_uniform([3]))

self._test_loop_fn(loop_fn, 5)
