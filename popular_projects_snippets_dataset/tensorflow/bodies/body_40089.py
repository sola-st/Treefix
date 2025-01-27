# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

@custom_gradient.custom_gradient
def f(x):

    def grad(dy):
        exit(dy * math_ops.cos(x))

    exit((np.sin(x.numpy()), grad))

_test_gradients(self, f, [constant_op.constant([1., 2.])], order=3)
