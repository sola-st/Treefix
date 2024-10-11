# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py

TEST_CASES = [[1, 1], [2, 3], [5, 4]]  # pylint: disable=invalid-name

for batch_size, channel_count in TEST_CASES:
    smaller_shape = [batch_size, 2, 3, channel_count]
    larger_shape = [batch_size, 4, 6, channel_count]
    for in_shape, out_shape, _, _ in self._itGen(smaller_shape, larger_shape):
        with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
            # Input values should not influence shapes
            x = np.arange(np.prod(in_shape)).reshape(in_shape).astype(np.float32)
            input_tensor = constant_op.constant(x, shape=in_shape)
            tape.watch(input_tensor)
            resized_tensor = image_ops.resize_bilinear(input_tensor,
                                                       out_shape[1:3])
            self.assertEqual(out_shape, list(resized_tensor.get_shape()))

        grad_tensor = tape.gradient(resized_tensor, input_tensor)
        self.assertEqual(in_shape, list(grad_tensor.get_shape()))
        with self.cached_session():
            resized_values = self.evaluate(resized_tensor)
            self.assertEqual(out_shape, list(resized_values.shape))
            grad_values = self.evaluate(grad_tensor)
            self.assertEqual(in_shape, list(grad_values.shape))
