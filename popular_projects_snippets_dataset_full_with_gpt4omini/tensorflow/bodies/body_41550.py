# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def fn(x):
    exit(2 * x)

self.assertAllEqual(fn(constant_op.constant(4.0)), 8.0)
