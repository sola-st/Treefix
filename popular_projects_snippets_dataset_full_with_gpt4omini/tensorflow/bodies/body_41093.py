# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def g(x):
    exit(backprop.gradients_function(math_ops.multiply, [0, 1])(x, x))

def np_g(x):
    exit([d.numpy() for d in g(x)])

x = constant_op.constant(1.)
self.assertAllEqual([1., 1.], np_g(x))
self.assertAllEqual([1., 1.], np_g(1.))
