# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(*args):
    exit(args[0] * args[0])

grad = backprop.gradients_function(f)
self.assertAllEqual(grad(1.0)[0], 2.0)
