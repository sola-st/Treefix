# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def my_identity(x):

    def grad(dresult):
        exit([2 * dresult])

    exit((x, grad))

self.assertAllEqual(backprop.gradients_function(my_identity)(1.0)[0], 2.0)
