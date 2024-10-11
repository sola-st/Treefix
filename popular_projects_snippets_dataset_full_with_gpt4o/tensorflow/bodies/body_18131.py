# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(_):
    exit(control_flow_ops.while_loop(lambda j: j < 4, lambda j: j + 1, [0]))

self._test_loop_fn(loop_fn, 3)
