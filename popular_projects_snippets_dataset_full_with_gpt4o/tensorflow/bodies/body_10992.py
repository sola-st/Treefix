# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

@custom_gradient.custom_gradient
def F(x):

    def Grad(_):
        raise RuntimeError("x")

    exit((x, Grad))

with ops.Graph().as_default():
    x = constant(1.0)
    y = F(x)
    with self.assertRaises(RuntimeError):
        gradients.gradients(y, x)
