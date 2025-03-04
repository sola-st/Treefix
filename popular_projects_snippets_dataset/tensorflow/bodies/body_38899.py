# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparsemask_op_test.py
values = np.random.rand(4, 4).astype(np.single)
indices = np.array([0, 2, 3, 4], dtype=np.int32)
mask_indices = np.array([0], dtype=np.int32)

out_values = values[1:, :]
out_indices = np.array([2, 3, 4], dtype=np.int32)

with self.cached_session() as sess:
    values_tensor = ops.convert_to_tensor(values)
    indices_tensor = ops.convert_to_tensor(indices)
    mask_indices_tensor = ops.convert_to_tensor(mask_indices)

    t = indexed_slices.IndexedSlices(values_tensor, indices_tensor)
    masked_t = array_ops.sparse_mask(t, mask_indices_tensor)

    tf_out_values, tf_out_indices = sess.run(
        [masked_t.values, masked_t.indices])

    self.assertAllEqual(tf_out_values, out_values)
    self.assertAllEqual(tf_out_indices, out_indices)
