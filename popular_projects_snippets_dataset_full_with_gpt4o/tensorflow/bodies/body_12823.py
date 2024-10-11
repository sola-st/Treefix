# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = constant_op.constant(1)
with self.assertRaises(TypeError):
    control_flow_ops.cond(True, lambda: x)
