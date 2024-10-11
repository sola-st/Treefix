# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x):
    exit(math_ops.add(x, constant_op.constant(3)))

@polymorphic_function.function
def g(x):
    exit(f(f(x)))

self.assertAllEqual(8, g(constant_op.constant(2)))
