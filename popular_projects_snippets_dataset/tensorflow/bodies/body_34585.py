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

    # Test combined gradients + aggregation of read(0)
    grad = gradients_impl.gradients(
        ys=[r0], xs=[value], grad_ys=[[2.0, 3.0]])[0]
    read_val, grad_val = session.run([r0, grad])

    self.assertAllEqual([1.0, -1.0], read_val)
    self.assertAllEqual([[2.0, 3.0], [0.0, 0.0]], grad_val)
