# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    indices = np.array([[3, 2, 0], [4, 5, 1]]).astype(np.int64)
    values = np.array([1.0, 2.0]).astype(np.float32)
    shape = np.array([7, 9, 2]).astype(np.int64)
    sp = array_ops.sparse_placeholder(
        shape=[None, 9, 2], dtype=np.float32, name='placeholder1')
    sp_indices = array_ops.identity(sp.indices)
    sp_values = array_ops.identity(sp.values)
    sp_shape = array_ops.identity(sp.dense_shape)
    sp2 = sparse_tensor.SparseTensor(sp_indices, sp_values, sp_shape)
    # Feed with tuple
    indices_out, values_out, shape_out = s.run(
        [sp_indices, sp_values, sp_shape], {
            sp: (indices, values, shape)
        })
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # Feed with SparseTensorValue
    indices_out, values_out, shape_out = s.run(
        [sp_indices, sp_values, sp_shape], {
            sp: sparse_tensor.SparseTensorValue(indices, values, shape)
        })
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # Feed with SparseTensorValue, fetch SparseTensorValue
    sp2_out = s.run(sp2, {
        sp: sparse_tensor.SparseTensorValue(indices, values, shape)
    })
    self.assertAllEqual(sp2_out.indices, indices)
    self.assertAllEqual(sp2_out.values, values)
    self.assertAllEqual(sp2_out.dense_shape, shape)
