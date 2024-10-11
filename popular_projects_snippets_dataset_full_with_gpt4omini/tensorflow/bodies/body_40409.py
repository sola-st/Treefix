# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def mul(x):
    exit(math_ops._mul_dispatch(x, x))  # pylint: disable=protected-access

self.assertAllEqual(backprop.gradients_function(mul)(3.0)[0].numpy(), 6.0)
