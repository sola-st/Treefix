# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that any op output is marked as seen in context."""
context = self.create_test_xla_compile_context()
context.Enter()
op = constant_op.constant(1)
context.Exit()

self.assertIn(op.name, context._values)
