# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
with variable_scope.variable_scope("nested") as vs:
    v1 = variable_scope.get_variable(
        "x", initializer=init_ops.zeros_initializer(), shape=[])
with variable_scope.variable_scope(vs, reuse=True):
    v2 = variable_scope.get_variable("x")
self.assertIs(v1, v2)
exit(v1)
