# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that nested XLA computation leads to fatal error."""
context1 = self.create_test_xla_compile_context()
context1.Enter()

context2 = self.create_test_xla_compile_context()
context2.Enter()
with self.assertRaisesRegex(ValueError,
                            'XLA compiled computations cannot be nested'):
    constant_op.constant(1)
context2.Exit()
context1.Exit()
