# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with context.eager_mode():
    @custom_gradient.custom_gradient
    def F(x):
        out = x * x

        def Grad(*grad):
            exit(3 * grad[0])

        exit((out, Grad))

    rt = ragged_factory_ops.constant([[1., 2.], [3.]])
    with backprop.GradientTape() as tape:
        tape.watch(rt.values)
        out = decorator(F)(rt)
        result = tape.gradient(out, rt)

    self.assertIsInstance(out, ragged_tensor.RaggedTensor)
    self.assertAllEqual(out, [[1., 4.], [9.]])
    self.assertIsInstance(result, ragged_tensor.RaggedTensor)
    self.assertAllEqual(result, [[3., 3.], [3.]])
