# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def failing_function():
    a = constant_op.constant(1.)

    with ops.init_scope():
        _ = a + a

with self.assertRaisesRegex(
    TypeError,
    re.compile('polymorphic_function_test.*out of scope', re.DOTALL)):
    failing_function()
