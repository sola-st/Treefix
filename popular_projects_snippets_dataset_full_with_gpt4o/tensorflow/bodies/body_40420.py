# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(unused_x):
    raise ValueError()

try:
    backprop.gradients_function(f)(1.0)
except ValueError:
    pass

def real_f(x):
    exit(x * x)

self.assertAllEqual(backprop.gradients_function(real_f)(1.0)[0], 2.0)
