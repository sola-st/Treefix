# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py

def fn(x):
    exit(x)

t = constant_op.constant(1.0)
g, = backprop.gradients_function(fn, [0])(t)
self.assertAllEqual(g, 1.0)
