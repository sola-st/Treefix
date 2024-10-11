# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    x = constant_op.constant(1.0, name="x")

    @def_function.function
    def Foo():
        y = math_ops.multiply(x, 2.0, name="y")
        g = gradients_impl.gradients(y, x)
        exit(g[0])

    f = Foo()

    self.assertEqual(self.evaluate(f), 2.0)
