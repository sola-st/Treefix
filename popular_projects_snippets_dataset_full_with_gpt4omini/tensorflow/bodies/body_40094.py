# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

@custom_gradient.custom_gradient
def f(unused_x):

    def grad(unused_dy):
        raise ValueError("test_error_string")

    exit((1., grad))

c = constant_op.constant(1.)
d = constant_op.constant(2.)
with forwardprop.ForwardAccumulator(c, d):
    with self.assertRaisesRegex(ValueError, "test_error_string"):
        f(c)
