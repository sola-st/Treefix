# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
with self.cached_session(use_gpu=False) as sess:
    sp_input = self._SparseTensorValue_5x6(np.arange(6))
    serialized = serialize_fn(sp_input, out_type=out_type)
    serialized = array_ops.stack([serialized, serialized])
    serialized = array_ops.stack([serialized, serialized])

    sp_deserialized = deserialize_fn(serialized, dtype=dtypes.int32)

    combined_indices, combined_values, combined_shape = sess.run(
        sp_deserialized)

    # minibatch 0
    self.assertAllEqual(combined_indices[:6, :2], [[0, 0]] * 6)
    self.assertAllEqual(combined_indices[:6, 2:], sp_input[0])
    self.assertAllEqual(combined_values[:6], sp_input[1])
    # minibatch 1
    self.assertAllEqual(combined_indices[6:12, :2], [[0, 1]] * 6)
    self.assertAllEqual(combined_indices[6:12, 2:], sp_input[0])
    self.assertAllEqual(combined_values[6:12], sp_input[1])
    # minibatch 2
    self.assertAllEqual(combined_indices[12:18, :2], [[1, 0]] * 6)
    self.assertAllEqual(combined_indices[12:18, 2:], sp_input[0])
    self.assertAllEqual(combined_values[12:18], sp_input[1])
    # minibatch 3
    self.assertAllEqual(combined_indices[18:, :2], [[1, 1]] * 6)
    self.assertAllEqual(combined_indices[18:, 2:], sp_input[0])
    self.assertAllEqual(combined_values[18:], sp_input[1])

    self.assertAllEqual(combined_shape, [2, 2, 5, 6])
