# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that resource variable usage is allowed."""
a = variable_scope.get_variable(
    name='variable_a', use_resource=True, initializer=1)

context = self.create_test_xla_compile_context()
context.Enter()
a.assign(2)
context.Exit()
