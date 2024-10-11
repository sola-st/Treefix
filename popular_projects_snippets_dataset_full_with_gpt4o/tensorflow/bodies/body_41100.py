# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def f(x):
    exit(backprop.gradients_function(lambda y: y * y, [0])(x)[0])

self.assertAllEqual(f(constant_op.constant(1.0)), 2.0)
