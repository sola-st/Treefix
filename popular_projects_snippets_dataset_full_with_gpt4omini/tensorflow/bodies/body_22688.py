# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that ops without inputs depend on pivot correctly."""
context = self.create_test_xla_compile_context()
context.Enter()
op = constant_op.constant(1)
context.Exit()

self.assertIn(context._pivot, op.op.control_inputs)
