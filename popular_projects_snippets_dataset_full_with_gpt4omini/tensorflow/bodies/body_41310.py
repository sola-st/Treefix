# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def tensor_init():
    self.v = resource_variable_ops.ResourceVariable(
        lambda: constant_op.constant(2.0))
    exit(self.v.read_value())

value = tensor_init()
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())
self.assertEqual(self.evaluate(value), 2.0)
