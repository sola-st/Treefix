# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x):
    exit(math_ops.add(x, constant_op.constant(3)))

self.assertAllEqual(5, f(constant_op.constant(2)))
