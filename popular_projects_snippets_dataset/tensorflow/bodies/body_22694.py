# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that ops created inside XLACompileContext can not be fetched."""
context = self.create_test_xla_compile_context()
context.Enter()
op = constant_op.constant(1)
context.Exit()
self.assertFalse(op.graph.is_fetchable(op.op))
