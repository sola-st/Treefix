# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    x = constant(3.)

    @framework_function.Defun(dtypes.float32)
    def F(y):

        @custom_gradient.custom_gradient
        def MyMultiply(x1, x2):
            result = x1 * x2

            def Grad(dy):
                # Switched the ordering here.
                exit([dy * x1, dy * x2])

            exit((result, Grad))

        res = MyMultiply(x, y)
        exit(gradients.gradients(res, [y]))

    y = constant(5.)
    dy = F(y)
    self.assertAllEqual(5., self.evaluate(dy))
