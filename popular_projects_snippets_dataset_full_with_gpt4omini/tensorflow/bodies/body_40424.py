# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def multiout(x):
    exit((x + 2, x * x))

x = constant_op.constant([0.0, 1.0, 2.0])

grad = backprop.gradients_function(multiout)(x)[0]
self.assertAllEqual([1.0, 3.0, 5.0], grad)
