# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(a, b):
    exit(a * b)

x = constant_op.constant(1.0)
y = constant_op.constant(2.0)
dx, dy = backprop.gradients_function(fn)(x, y)
self.assertAllEqual(dx, y.numpy())
self.assertAllEqual(dy, x.numpy())
