# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that non-resource variable usage is disallowed."""
a = variable_scope.get_variable(
    name='variable_a', shape=(1), use_resource=False)

context = self.create_test_xla_compile_context()
context.Enter()
with self.assertRaisesRegex(
    NotImplementedError, 'Non-resource Variables are not supported inside '
    r'XLA computations \(operator name: Assign\)'):
    state_ops.assign(a, a + 1)
context.Exit()
