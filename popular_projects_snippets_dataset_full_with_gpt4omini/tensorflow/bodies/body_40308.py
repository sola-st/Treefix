# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def f(x):
    (y,) = backprop.gradients_function(lambda x: x * x)(x)

    def grad(dy):
        exit([2 * dy])

    exit((y, grad))

self.assertAllEqual(f(1.0), 2.0)
