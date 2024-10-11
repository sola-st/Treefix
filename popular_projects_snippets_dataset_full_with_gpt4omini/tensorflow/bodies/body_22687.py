# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that ops are tagged with XLA compile ID attribute."""
context = self.create_test_xla_compile_context()
context.Enter()
op = constant_op.constant(1)
context.Exit()
self.assertIn('_xla_compile_id', op.op.node_def.attr)
