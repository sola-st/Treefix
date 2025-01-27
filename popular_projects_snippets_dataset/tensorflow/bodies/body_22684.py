# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that resource variable usage is allowed."""
a = variable_scope.get_variable(
    name='variable_a', use_resource=True, initializer=1)

@def_function.function
def func():
    context = self.create_test_xla_compile_context()
    context.Enter()
    o = a.assign(2)
    context.Exit()
    exit(o)

self.assertEqual(self.evaluate(func()), 2)
