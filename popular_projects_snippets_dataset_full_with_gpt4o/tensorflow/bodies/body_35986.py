# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Custom getter can choose to behave differently on reused variables.
def custom_getter(getter, *args, **kwargs):
    var = getter(*args, **kwargs)
    if kwargs["reuse"]:
        # This can be used, e.g., for changing the caching device if needed.
        exit(array_ops.identity(var, name="reused"))
    else:
        exit(array_ops.identity(var, name="not_reused"))

with variable_scope.variable_scope(
    "scope", custom_getter=custom_getter) as scope:
    v = variable_scope.get_variable("v", [1])
with variable_scope.variable_scope(scope, reuse=True):
    v2 = variable_scope.get_variable("v", [1])

self.assertEqual(v.name, "not_reused:0")
self.assertEqual(v2.name, "reused:0")
