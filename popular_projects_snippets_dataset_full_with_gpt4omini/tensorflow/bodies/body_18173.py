# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    exit(control_flow_ops.while_loop(lambda j, x: j < 4, lambda j, x:
                                       (j + 1, x + i), [0, 0]))

self._test_loop_fn(loop_fn, 3)
