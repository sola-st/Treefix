# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
fn_none = lambda: None
fn_tensor = lambda: constant_op.constant(1)

with self.assertRaises(ValueError):
    control_flow_ops.cond(constant_op.constant(True), fn_none, fn_tensor)

with self.assertRaises(ValueError):
    control_flow_ops.cond(constant_op.constant(True), fn_tensor, fn_none)
