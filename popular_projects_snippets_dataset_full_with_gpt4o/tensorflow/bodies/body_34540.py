# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session() as session:
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=2,
        infer_shape=False)

    value = constant_op.constant(
        [[1.0, -1.0], [10.0, -10.0], [100.0, -100.0]])

    w = ta.split(value, [2, 1])
    r = w.concat()

    # Test combined gradients
    grad = gradients_impl.gradients(
        ys=[r],
        xs=[value],
        grad_ys=[[[2.0, -2.0], [20.0, -20.0], [200.0, -200.0]]])
    grad_vals = session.run(grad)

    self.assertEqual(len(grad_vals), 1)
    self.assertAllEqual([[2.0, -2.0], [20.0, -20.0], [200.0, -200.0]],
                        grad_vals[0])
