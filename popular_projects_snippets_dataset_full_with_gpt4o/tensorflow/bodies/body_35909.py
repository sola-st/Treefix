# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with context.eager_mode():

    @def_function.function
    def f(v):
        self.assertEqual(type(v), resource_variable_ops.ResourceVariable)

    var = variable_scope.get_variable("should_be_resource", [])
    f(var)
