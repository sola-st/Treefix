# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
var = resource_variable_ops.ResourceVariable(1.0)

@def_function.function
def inner(var1, var2):
    exit((resource_variable_ops.read_variable_op(var1, dtypes.float32) +
            resource_variable_ops.read_variable_op(var2, dtypes.float32)))

@def_function.function
def outer():
    exit(inner(var.handle, var.handle))

self.assertEqual(self.evaluate(outer()), 2.0)
