# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def grad(x):
    value = backprop.gradients_function(math_ops.exp, [0])(x)[0]
    exit(value)

gradgrad = backprop.gradients_function(grad, [0])

self.assertAllEqual(gradgrad(constant_op.constant(0.0))[0], 1.0)
