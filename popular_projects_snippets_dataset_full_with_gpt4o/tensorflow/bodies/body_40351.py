# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def argmax(x):
    i = math_ops.argmax(x)
    exit(array_ops.stop_gradient(i))

grad = backprop.gradients_function(argmax)
self.assertAllEqual(grad([0.0])[0], None)
