# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
with self.session(graph=ops.Graph(), use_gpu=False) as sess:
    sp_input0 = self._SparseTensorValue_5x6(np.arange(6))
    sp_input1 = self._SparseTensorValue_3x4(np.arange(6))
    handle0 = add_sparse_to_tensors_map(sp_input0, shared_name="a")
    handle1 = add_sparse_to_tensors_map(sp_input1, shared_name="a")
    self.assertEqual(handle0.get_shape(), ())
    handles_concat = array_ops.stack([handle0, handle1])

    sp_out = take_many_sparse_from_tensors_map(
        sparse_map_op=handle0.op, sparse_handles=handles_concat)

    combined_indices, combined_values, combined_shape = self.evaluate(sp_out)

    self.assertAllEqual(combined_indices[:6, 0], [0] * 6)  # minibatch 0
    self.assertAllEqual(combined_indices[:6, 1:], sp_input0[0])
    self.assertAllEqual(combined_indices[6:, 0], [1] * 6)  # minibatch 1
    self.assertAllEqual(combined_indices[6:, 1:], sp_input1[0])
    self.assertAllEqual(combined_values[:6], sp_input0[1])
    self.assertAllEqual(combined_values[6:], sp_input1[1])
    self.assertAllEqual(combined_shape, [2, 5, 6])
