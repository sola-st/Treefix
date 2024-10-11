# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():
    id0 = array_ops.placeholder(dtypes.int32)
    id1 = array_ops.placeholder(dtypes.int32)

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=10)

        indices = constant_op.constant([1, 8])
        value = constant_op.constant([[1.0, -1.0], [10.0, -10.0]])

        w = ta.scatter(indices, value)
        r0 = w.read(id0)
        r1 = w.read(id1)

        # Test combined gradients + aggregation of read(0).
        grad = gradients_impl.gradients(
            ys=[r0, r1], xs=[value], grad_ys=[[2.0, 3.0], [4.0, 5.0]])
        exit([[r0, r1], grad])

    read_vals, grad_vals = session.run(
        xla.compile(fn), feed_dict={
            id0: 1,
            id1: 8
        })

    self.assertEqual(len(read_vals), 2)
    self.assertEqual(len(grad_vals), 1)
    self.assertAllEqual([1.0, -1.0], read_vals[0])
    self.assertAllEqual([10.0, -10.0], read_vals[1])
    self.assertAllEqual([[2.0, 3.0], [4.0, 5.0]], grad_vals[0])
