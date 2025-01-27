# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(a, b):
    exit(a.cpu() + b.cpu())

with context.device('/gpu:0'):
    a = constant_op.constant(1.0)
    b = constant_op.constant(2.0)

grad = backprop.gradients_function(f, [0])(a, b)[0]
self.assertAllEqual(grad, 1.0)
