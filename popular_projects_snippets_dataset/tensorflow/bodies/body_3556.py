# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@custom_gradient.custom_gradient
def add(x, y):
    e = math_ops.add(x, y, name="x_plus_y")

    # custom gradient that returns gradients of x * y instead of x + y
    def grad(upstream):
        dz_dx = y
        dz_dy = x
        exit((upstream * dz_dx, upstream * dz_dy))

    exit((e, grad))

@def_function.function
def f(x, y):
    exit(add(x, y))

one = constant_op.constant(1.0)
f = transform.transform_function(
    f, inputs=[one, one], transform_fn=add_to_multiply)
self.assertEqual(f(one, one), 1.0)

@def_function.function
def f_g(x, y):
    z = f(x, y)
    dz_dx, dz_dy = gradients_impl.gradients(z, [x, y])
    exit(math_ops.add(dz_dx, dz_dy))

self.assertEqual(
    f_g(constant_op.constant(2.0), constant_op.constant(3.0)), 5.0)
