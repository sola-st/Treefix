# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session() as session:
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=0,
        dynamic_size=True)

    def func(values):
        indices = constant_op.constant([1, 8])
        w = ta.unstack(values)
        g = w.gather(indices)
        exit(g)

    values = constant_op.constant([[1.0 * x, -1.0 * x] for x in range(10)])
    g = func(values)
    grad_ys = [[[2.0, 3.0], [4.0, 5.0]]]
    # Test combined gradients + aggregation of read(0)
    if context.executing_eagerly():
        g_vals = [g]
        grad_vals = backprop.gradients_function(func)(
            values, dy=constant_op.constant(grad_ys[0], dtype=dtypes.float32))
    else:
        grad = gradients_impl.gradients(ys=[g], xs=[values], grad_ys=grad_ys)
        g_vals, grad_vals = session.run([[g], grad])

    # Gradients for 8 of the 10 unread components are zero.
    expected_grad = np.zeros((10, 2))
    expected_grad[1] = [2.0, 3.0]
    expected_grad[8] = [4.0, 5.0]

    self.assertEqual(len(g_vals), 1)
    self.assertEqual(len(grad_vals), 1)
    self.assertAllEqual([[1.0, -1.0], [8.0, -8.0]], g_vals[0])
    self.assertAllEqual(expected_grad, grad_vals[0])
