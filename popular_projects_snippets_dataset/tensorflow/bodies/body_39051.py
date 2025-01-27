# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
with self.session(use_gpu=False) as sess:
    # N == 4 because shape_value == [4, 5]
    indices_value = np.array([[0, 0], [0, 1], [2, 0]], dtype=np.int64)
    values_value = np.array([b"a", b"b", b"c"])
    shape_value = np.array([4, 5], dtype=np.int64)
    sparse_tensor = self._SparseTensorPlaceholder(dtype=dtypes.string)
    handles = add_many_sparse_to_tensors_map(sparse_tensor)
    roundtrip = take_many_sparse_from_tensors_map(
        sparse_map_op=handles.op, sparse_handles=handles)
    handles_value, roundtrip_value = sess.run(
        [handles, roundtrip],
        feed_dict={
            sparse_tensor.indices: indices_value,
            sparse_tensor.values: values_value,
            sparse_tensor.dense_shape: shape_value
        })
    self.assertEqual(handles_value.shape, (4,))
    self.assertAllEqual(roundtrip_value.indices, indices_value)
    self.assertAllEqual(roundtrip_value.values, values_value)
    self.assertAllEqual(roundtrip_value.dense_shape, shape_value)
