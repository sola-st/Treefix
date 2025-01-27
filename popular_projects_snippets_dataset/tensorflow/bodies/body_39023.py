# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
with self.cached_session(use_gpu=False) as sess:
    # N == 4 because shape_value == [4, 5]
    indices_value = np.array([[0, 0], [0, 1], [2, 0]], dtype=np.int64)
    values_value = np.array([b"a", b"b", b"c"])
    shape_value = np.array([4, 5], dtype=np.int64)
    sparse_tensor = self._SparseTensorPlaceholder(dtype=dtypes.string)
    serialized = serialize_many_fn(sparse_tensor, out_type=out_type)
    serialized_value = sess.run(
        serialized,
        feed_dict={
            sparse_tensor.indices: indices_value,
            sparse_tensor.values: values_value,
            sparse_tensor.dense_shape: shape_value
        })
    self.assertEqual(serialized_value.shape, (4, 3))
