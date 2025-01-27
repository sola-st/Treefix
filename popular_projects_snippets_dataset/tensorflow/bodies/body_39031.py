# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
with self.session(use_gpu=False) as sess:
    indices_value = np.array([[]], dtype=np.int64)
    values_value = np.array([37], dtype=np.int32)
    shape_value = np.array([], dtype=np.int64)
    sparse_tensor = self._SparseTensorPlaceholder()
    serialized = sparse_ops.serialize_sparse(
        sparse_tensor, out_type=dtypes.variant)
    stacked = array_ops.stack([serialized, serialized])
    deserialized = sparse_ops.deserialize_sparse(stacked, dtype=dtypes.int32)
    deserialized_value = sess.run(
        deserialized,
        feed_dict={
            sparse_tensor.indices: indices_value,
            sparse_tensor.values: values_value,
            sparse_tensor.dense_shape: shape_value
        })
    self.assertAllEqual(deserialized_value.indices,
                        np.array([[0], [1]], dtype=np.int64))
    self.assertAllEqual(deserialized_value.values,
                        np.array([37, 37], dtype=np.int32))
    self.assertAllEqual(deserialized_value.dense_shape,
                        np.array([2], dtype=np.int64))
