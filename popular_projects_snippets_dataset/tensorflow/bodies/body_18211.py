# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with ops.Graph().as_default():
    x = constant_op.constant(1.0)
    self._run(x, 10000, name="session_run_overhead")
