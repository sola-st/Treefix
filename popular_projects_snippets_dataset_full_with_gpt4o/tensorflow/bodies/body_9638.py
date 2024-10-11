# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    values = np.array([1.0, 2.0]).astype(np.float32)
    indices = np.array([[3, 2, 0], [4, 5, 1]]).astype(np.int64)
    dense_shape = np.array([7, 9, 2]).astype(np.int64)
    ind = indexed_slices.IndexedSlices(
        array_ops.placeholder(dtype=np.float32, shape=(2,)),
        array_ops.placeholder(dtype=np.int64, shape=(2, 3)),
        array_ops.placeholder(dtype=np.int64, shape=(3,)),
    )
    ind_values = array_ops.identity(ind.values)
    ind_indices = array_ops.identity(ind.indices)
    ind_dense_shape = array_ops.identity(ind.dense_shape)
    ind2 = indexed_slices.IndexedSlices(ind_values, ind_indices,
                                        ind_dense_shape)
    # Feed with tuple
    values_out, indices_out, dense_shape_out = s.run(
        [ind_values, ind_indices, ind_dense_shape], {
            ind: (values, indices, dense_shape)
        })
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(dense_shape_out, dense_shape)
    # Feed with IndexedSlicesValue
    values_out, indices_out, dense_shape_out = s.run([
        ind_values, ind_indices, ind_dense_shape
    ], {ind: indexed_slices.IndexedSlicesValue(values, indices, dense_shape)})
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(dense_shape_out, dense_shape)
    # Feed with IndexedSlicesValue, fetch IndexedSlicesValue
    ind2_out = s.run(ind2, {
        ind: indexed_slices.IndexedSlicesValue(values, indices, dense_shape)
    })
    self.assertAllEqual(ind2_out.values, values)
    self.assertAllEqual(ind2_out.indices, indices)
    self.assertAllEqual(ind2_out.dense_shape, dense_shape)
