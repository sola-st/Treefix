# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def f(x):
    exit(math_ops.add(x, x))

@polymorphic_function.function
def g(x):
    exit(backprop.gradients_function(f, [0])(x)[0])

self.assertAllEqual(2, g(constant_op.constant(2.)))
