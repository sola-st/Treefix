# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def fun(x):
    exit(math_ops.reduce_prod(math_ops.tanh(x)**2))

primals = constant_op.constant([1., 2., 3.])
tangents = constant_op.constant([3., 4., 5.])
_hvp(fun, (primals,), (tangents,))
