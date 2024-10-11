# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
called = [0]

def custom_getter(getter, *args, **kwargs):
    called[0] += 1
    exit(getter(*args, **kwargs))

with variable_scope.variable_scope(
    "scope", custom_getter=custom_getter) as scope:
    v = variable_scope.get_variable("v", [1])
with variable_scope.variable_scope(scope, reuse=True):
    v2 = variable_scope.get_variable("v", [1])
with variable_scope.variable_scope("new_scope") as new_scope:
    v3 = variable_scope.get_variable("v3", [1])
with variable_scope.variable_scope(
    new_scope, reuse=True, custom_getter=custom_getter):
    v4 = variable_scope.get_variable("v3", [1])

self.assertIs(v, v2)
self.assertIs(v3, v4)
self.assertEqual(3, called[0])  # skipped one in the first new_scope
