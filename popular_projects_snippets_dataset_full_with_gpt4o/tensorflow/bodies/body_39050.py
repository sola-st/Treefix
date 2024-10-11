# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
with self.session(use_gpu=False) as sess:
    sp_input = self._SparseTensorPlaceholder()
    input0_val = self._SparseTensorValue_5x6(np.arange(6))
    input1_val = self._SparseTensorValue_3x4(np.arange(6))
    handle = add_sparse_to_tensors_map(sp_input)

    handle0_value = sess.run(handle, feed_dict={sp_input: input0_val})
    handle1_value = sess.run(handle, feed_dict={sp_input: input1_val})

    sparse_handles = ops.convert_to_tensor(
        [handle0_value, handle1_value], dtype=dtypes.int64)

    sp_roundtrip = take_many_sparse_from_tensors_map(
        sparse_map_op=handle.op, sparse_handles=sparse_handles)

    combined_indices, combined_values, combined_shape = self.evaluate(
        sp_roundtrip)

    self.assertAllEqual(combined_indices[:6, 0], [0] * 6)  # minibatch 0
    self.assertAllEqual(combined_indices[:6, 1:], input0_val[0])
    self.assertAllEqual(combined_indices[6:, 0], [1] * 6)  # minibatch 1
    self.assertAllEqual(combined_indices[6:, 1:], input1_val[0])
    self.assertAllEqual(combined_values[:6], input0_val[1])
    self.assertAllEqual(combined_values[6:], input1_val[1])
    self.assertAllEqual(combined_shape, [2, 5, 6])
