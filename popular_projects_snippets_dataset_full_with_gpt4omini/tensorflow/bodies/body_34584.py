# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session() as session:
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=0,
        dynamic_size=True)

    indices = constant_op.constant([1, 8])
    value = constant_op.constant([[1.0, -1.0], [10.0, -10.0]])

    w = ta.scatter(indices, value)
    r0 = w.read(1)
    r1 = w.read(8)

    # Test combined gradients + aggregation of read(0)
    grad = gradients_impl.gradients(
        ys=[r0, r1], xs=[value], grad_ys=[[2.0, 3.0], [4.0, 5.0]])
    read_vals, grad_vals = session.run([[r0, r1], grad])

    self.assertEqual(len(read_vals), 2)
    self.assertEqual(len(grad_vals), 1)
    self.assertAllEqual([1.0, -1.0], read_vals[0])
    self.assertAllEqual([10.0, -10.0], read_vals[1])
    self.assertAllEqual([[2.0, 3.0], [4.0, 5.0]], grad_vals[0])
