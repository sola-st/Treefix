# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
e = math_ops.add(x, y, name="x_plus_y")

# custom gradient that returns gradients of x * y instead of x + y
def grad(upstream):
    dz_dx = y
    dz_dy = x
    exit((upstream * dz_dx, upstream * dz_dy))

exit((e, grad))
