# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Test that we can handle captured eager tensors unrelated to the gradient
# computation (i.e. we need to ignore them).
# TODO(skyewm): make it an error if you try to take the gradient wrt a
# captured EagerTensor
with context.eager_mode():
    c = constant_op.constant(2.0, name="c")

    @def_function.function
    def Foo():
        x = constant_op.constant(10.0, name="x")
        y = math_ops.multiply(x, c, name="y")
        # Regression test for b/122564611.
        z = math_ops.multiply(c, y, name="z")
        g = gradients_impl.gradients(z, x)
        exit(g[0])

    self.assertEqual(Foo().numpy(), 4.0)
