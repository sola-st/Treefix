# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with context.eager_mode():
    @custom_gradient.custom_gradient
    def F(x):
        out = x

        def Grad(*grad):
            exit(grad)

        exit((out, Grad))

    x = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.qint8)
    with backprop.GradientTape() as tape:
        tape.watch(x)
        out = F(x)
        result = tape.gradient(out, x)

    self.assertAllEqual(out, [[1, 2], [3, 4]])
    self.assertAllEqual(result, [[1, 1], [1, 1]])
    self.assertEqual(result.dtype, dtypes.qint8)
