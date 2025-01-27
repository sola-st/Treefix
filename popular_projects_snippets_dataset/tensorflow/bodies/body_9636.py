# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    indices = np.array([[3, 2, 0], [4, 5, 1]]).astype(np.int64)
    values = np.array([1.0, 2.0]).astype(np.float32)
    shape = np.array([7, 9, 2]).astype(np.int64)
    sp = array_ops.sparse_placeholder(
        dtype=np.float32, shape=shape, name='placeholder1')
    self.assertAllEqual(sp.dense_shape.eval(session=s), shape)
    self.assertAllEqual(tensor_util.constant_value(sp.shape), shape)
    sp_indices = array_ops.identity(sp.indices)
    sp_values = array_ops.identity(sp.values)
    sp_shape = array_ops.identity(sp.dense_shape)
    # Feed with tuple
    indices_out, values_out, shape_out = s.run(
        [sp_indices, sp_values, sp_shape], {
            sp: (indices, values)
        })
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
