# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x, y):
    exit(x * y)

part = functools.partial(f, constant_op.constant(2.0))
self.assertAllEqual(
    backprop.gradients_function(part)(constant_op.constant(1.0))[0], 2.0)
