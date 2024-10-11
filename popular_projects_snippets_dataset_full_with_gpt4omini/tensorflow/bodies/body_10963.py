# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with self.cached_session():
    numpy_list = []
    dense_list = []
    sparse_list = []
    for _ in range(3):
        np_val = np.random.rand(4, 4, 4, 4).astype(np.float32)
        c = constant_op.constant(np_val)
        c_sparse = math_ops._as_indexed_slices(c)
        numpy_list.append(np_val)
        dense_list.append(c)
        sparse_list.append(c_sparse)
    packed_dense = array_ops.stack(dense_list)
    packed_sparse = array_ops.stack(sparse_list)
    self.assertAllClose(packed_dense, self.evaluate(packed_sparse))
