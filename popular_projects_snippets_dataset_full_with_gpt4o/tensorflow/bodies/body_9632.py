# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    indices = np.array([[3, 2, 0], [4, 5, 1]]).astype(np.int64)
    values = np.array([1.0, 2.0]).astype(np.float32)
    shape = np.array([7, 9, 2]).astype(np.int64)
    sp = sparse_tensor.SparseTensor(
        constant_op.constant(indices), constant_op.constant(values),
        constant_op.constant(shape))
    # Single fetch, use as tuple
    sp_out = s.run(sp)
    indices_out, values_out, shape_out = sp_out
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # Single fetch, use as SparseTensorValue
    sp_out = s.run(sp)
    self.assertAllEqual(sp_out.indices, indices)
    self.assertAllEqual(sp_out.values, values)
    self.assertAllEqual(sp_out.dense_shape, shape)
    # Tuple fetch, use as tuple
    indices_out, values_out, shape_out = s.run(sp)
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # List fetch, use as tuple
    (indices_out, values_out, shape_out), = s.run([sp])
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # List fetch, use as SparseTensorValue
    sp_out, = s.run([sp])
    self.assertAllEqual(sp_out.indices, indices)
    self.assertAllEqual(sp_out.values, values)
    self.assertAllEqual(sp_out.dense_shape, shape)
    # Dict fetch (single value), use as tuple
    indices_out, values_out, shape_out = s.run({'sp': sp})['sp']
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # Dict fetch (list value), use as tuple
    (indices_out, values_out, shape_out), = s.run({'sp': [sp]})['sp']
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # Dict fetch, use as SparseTensorValue
    sp_out = s.run({'sp': sp})['sp']
    self.assertAllEqual(sp_out.indices, indices)
    self.assertAllEqual(sp_out.values, values)
    self.assertAllEqual(sp_out.dense_shape, shape)
    # Nested list fetch use as tuple
    sp_out = s.run([[[sp]], sp])
    indices_out, values_out, shape_out = sp_out[0][0][0]
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    indices_out, values_out, shape_out = sp_out[1]
    self.assertAllEqual(indices_out, indices)
    self.assertAllEqual(values_out, values)
    self.assertAllEqual(shape_out, shape)
    # Nested list fetch, use as SparseTensorValue
    sp_out = s.run([[[sp]], sp])
    self.assertAllEqual(sp_out[0][0][0].indices, indices)
    self.assertAllEqual(sp_out[0][0][0].values, values)
    self.assertAllEqual(sp_out[0][0][0].dense_shape, shape)
    self.assertAllEqual(sp_out[1].indices, indices)
    self.assertAllEqual(sp_out[1].values, values)
    self.assertAllEqual(sp_out[1].dense_shape, shape)
