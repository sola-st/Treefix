# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=10)

        values = constant_op.constant([[1.0 * x, -1.0 * x] for x in range(10)])
        indices = constant_op.constant([1, 8])

        w = ta.unstack(values)
        g = w.gather(indices)

        # Test combined gradients + aggregation of read(0).
        grad = gradients_impl.gradients(
            ys=[g], xs=[values], grad_ys=[[[2.0, 3.0], [4.0, 5.0]]])
        exit([[g], grad])

    g_vals, grad_vals = self.evaluate(xla.compile(fn))

    # Gradients for 8 of the 10 unread components are zero.
    expected_grad = np.zeros((10, 2))
    expected_grad[1] = [2.0, 3.0]
    expected_grad[8] = [4.0, 5.0]

    self.assertEqual(len(g_vals), 1)
    self.assertEqual(len(grad_vals), 1)
    self.assertAllEqual([[1.0, -1.0], [8.0, -8.0]], g_vals[0])
    self.assertAllEqual(expected_grad, grad_vals[0])
