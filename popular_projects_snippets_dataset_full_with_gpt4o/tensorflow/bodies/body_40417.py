# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x):
    exit((x, 2 * x))

self.assertAllEqual(backprop.gradients_function(f)(1.0)[0], 3.0)
