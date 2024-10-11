# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
# Note: where is special because only some of its arguments are of
# differentiable dtypes.

def f(x):
    exit(array_ops.where(x < 10, x, x * x))

g = backprop.gradients_function(f)

self.assertAllEqual(g(5.)[0], 1.0)
self.assertAllEqual(g(50.)[0], 100.0)
