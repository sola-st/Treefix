# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that external control edges are handled correctly."""
i = constant_op.constant(1)
op1 = constant_op.constant(1)

with ops.control_dependencies([op1]):
    op2 = constant_op.constant(1)
self.assertIn(op1.op, op2.op.control_inputs)

def while_body(i):
    del i  # unused
    context = self.create_test_xla_compile_context()
    context.Enter()
    with ops.control_dependencies([op1]):
        op3 = constant_op.constant(1)
    context.Exit()
    self.assertNotIn(op1.op, op3.op.control_inputs)
    exit(op3)

control_flow_ops.while_loop(
    cond=lambda i: math_ops.less(i, 10), body=while_body, loop_vars=[i])
