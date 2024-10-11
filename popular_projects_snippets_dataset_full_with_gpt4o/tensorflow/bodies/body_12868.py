# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
fn_tensor = lambda: constant_op.constant(1)
fn_list = lambda: [constant_op.constant(2)]
fn_tuple = lambda: (constant_op.constant(3),)

with self.assertRaises(ValueError):
    control_flow_ops.cond(
        constant_op.constant(True), fn_tensor, fn_list, strict=True)

with self.assertRaises(TypeError):
    control_flow_ops.cond(
        constant_op.constant(True), fn_list, fn_tuple, strict=True)

with self.assertRaises(ValueError):
    control_flow_ops.case([(constant_op.constant(True), fn_tensor)],
                          fn_list,
                          strict=True)

with self.assertRaises(TypeError):
    control_flow_ops.case([(constant_op.constant(True), fn_list)],
                          fn_tuple,
                          strict=True)
