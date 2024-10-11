# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    x1 = constant_op.constant(1.0, name="x1")
    x2 = constant_op.constant(2.0, name="x2")
    x3 = math_ops.multiply(x1, x2, name="x3")

    @def_function.function
    def Outer():
        outer1 = array_ops.identity(x1, name="outer1")

        @def_function.function
        def Inner():
            inner1 = array_ops.identity(outer1, name="inner1")
            inner2 = array_ops.identity(x2, name="inner2")
            inner3 = array_ops.identity(x3, name="inner3")
            exit(gradients_impl.gradients([inner1, inner2, inner3, x1],
                                            [x1, x2]))

        exit(Inner())

    x1_grad, x2_grad = Outer()

    # 1.0 + None + 2.0 + 1.0 = 4.0
    self.assertEqual(self.evaluate(x1_grad), 4.0)
    # None + 1.0 + 1.0 + None = 2.0
    self.assertEqual(self.evaluate(x2_grad), 2.0)
