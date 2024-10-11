# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(_):
    exit(_ + _)

self.assertAllEqual(2.0, f(constant_op.constant(1.0)))
