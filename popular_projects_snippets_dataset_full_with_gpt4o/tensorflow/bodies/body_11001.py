# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with context.eager_mode():
    @custom_gradient.custom_gradient
    def F(x, y):
        out = (x * x, 2 * y)

        def Grad(*grad):
            exit((3 * grad[0], 4 * grad[1]))

        exit((out, Grad))

    rt1 = ragged_factory_ops.constant([[1., 2.], [3.]])
    rt2 = ragged_factory_ops.constant([[4.], [5., 6.]])
    with backprop.GradientTape() as tape:
        tape.watch((rt1, rt2))
        out1, out2 = decorator(F)(rt1, rt2)
        grad1, grad2 = tape.gradient((out1, out2), (rt1, rt2))

    self.assertIsInstance(out1, ragged_tensor.RaggedTensor)
    self.assertAllEqual(out1, [[1., 4.], [9.]])
    self.assertIsInstance(out2, ragged_tensor.RaggedTensor)
    self.assertAllEqual(out2, [[8.], [10., 12.]])
    self.assertIsInstance(grad1, ragged_tensor.RaggedTensor)
    self.assertAllEqual(grad1, [[3., 3.], [3.]])
    self.assertIsInstance(grad2, ragged_tensor.RaggedTensor)
    self.assertAllEqual(grad2, [[4.], [4., 4.]])
