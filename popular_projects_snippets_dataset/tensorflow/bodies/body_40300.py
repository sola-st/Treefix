# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x):
    exit(x)

grad_fn = backprop.gradients_function(f)
self.assertAllEqual(2., grad_fn(1., dy=2.)[0])
