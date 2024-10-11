# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
expected_constant = np.reshape(np.arange(24, dtype=np.int64), (3, 4, 2))
tensor = constant_op.constant(expected_constant)
sparse = sparse_ops.from_dense(tensor)
dense = sparse_ops.sparse_to_dense(sparse.indices, sparse.dense_shape,
                                   sparse.values)
constant = self.evaluate(dense)
self.assertAllEqual(expected_constant, constant)
