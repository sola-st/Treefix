# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that XLACompileContext is recognized as an XLA context."""
op1 = constant_op.constant(1)
context = self.create_test_xla_compile_context()
context.Enter()
op2 = constant_op.constant(2)
context.Exit()
self.assertFalse(control_flow_util.IsInXLAContext(op1.op))
self.assertTrue(control_flow_util.IsInXLAContext(op2.op))
