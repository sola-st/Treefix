# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def identity(x):

    def grad(_):
        exit([])  # This return value is wrong!

    exit((x, grad))

x = variables.Variable(1.0)
with backprop.GradientTape() as t:
    y = identity(x)
with self.assertRaises(ValueError):
    t.gradient(y, [x])
