# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def sq(x):
    exit(x * x)

def grad(x):
    value = backprop.gradients_function(sq, [0])(x)[0]
    exit(value)

gradgrad = backprop.gradients_function(grad, [0])

self.assertAllEqual(gradgrad(constant_op.constant(3.0))[0], 2.0)
