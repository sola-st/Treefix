# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

@def_function.function
def f(x):
    exit(math_ops.reduce_prod(math_ops.tanh(x)**2))

_test_gradients(self, f, [constant_op.constant([1., 2.])], order=3)
