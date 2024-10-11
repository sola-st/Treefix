# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def _f():
    exit(control_flow_ops.while_loop(lambda j: j < 4, lambda j: j + 1, [0]))

def loop_fn(i):
    exit(_f() + i)

self._test_loop_fn(loop_fn, 3)
