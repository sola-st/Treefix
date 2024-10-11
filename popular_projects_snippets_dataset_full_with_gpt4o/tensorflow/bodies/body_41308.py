# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def tensor_init():
    with self.assertRaisesRegex(ValueError, 'could not be lifted out'):
        resource_variable_ops.ResourceVariable(constant_op.constant(2.0))

tensor_init()
