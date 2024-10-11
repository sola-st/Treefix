# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
indices = np.array([(2, 1), (0, 0)]).astype(np.int64)
values = np.array([10, 11]).astype(np.float32)
shape = [3, 2]
sparse_t = sparse_tensor.SparseTensor(indices, values, shape)

dense_t = np.array([[1] * 500, [2] * 500], dtype=np.float32)
expected_t = np.array([[11] * 500, [0] * 500, [20] * 500], dtype=np.float32)

self.assertAllClose(
    expected_t, sparse_ops.sparse_tensor_dense_matmul(sparse_t, dense_t))
