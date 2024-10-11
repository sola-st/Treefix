# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def f(x):
    pointwise = math_ops.sin(x) * math_ops.tan(x)
    exit(math_ops.reduce_prod(
        pointwise + math_ops.reduce_sum(pointwise), axis=1))

_test_gradients(
    self,
    f,
    [constant_op.constant([[2.0, 3.0], [1.0, 4.0]], dtype=dtypes.float64)],
    order=3)
