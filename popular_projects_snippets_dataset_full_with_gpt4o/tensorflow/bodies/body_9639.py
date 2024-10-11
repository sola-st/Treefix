# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    indices = np.array([[3, 2, 0], [4, 5, 1]]).astype(np.int64)
    values = np.array([1.0, 2.0]).astype(np.float32)
    dense_shape = None
    ind = indexed_slices.IndexedSlices(
        constant_op.constant(values), constant_op.constant(indices), None)
    # Single fetch, use as tuple
    ind_out = s.run(ind)
    values_out, indices_out, dense_shape_out = ind_out
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(dense_shape_out, dense_shape)
    # Single fetch, use as IndexedSlicesValue
    ind_out = s.run(ind)
    self.assertAllEqual(ind_out.values, values)
    self.assertAllEqual(ind_out.indices, indices)
    self.assertAllEqual(ind_out.dense_shape, dense_shape)
    # Tuple fetch, use as tuple
    values_out, indices_out, dense_shape_out = s.run(ind)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(dense_shape_out, dense_shape)
    # List fetch, use as tuple
    (values_out, indices_out, dense_shape_out), = s.run([ind])
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(dense_shape_out, dense_shape)
    # List fetch, use as IndexedSlicesValue
    ind_out, = s.run([ind])
    self.assertAllEqual(ind_out.values, values)
    self.assertAllEqual(ind_out.indices, indices)
    self.assertAllEqual(ind_out.dense_shape, dense_shape)
