# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
indices = np.array([[1, 10]]).astype(np.int64)
values = np.array([10]).astype(np.float32)
shape = [3, 2]
sparse_t = sparse_tensor.SparseTensor(indices, values, shape)

# Test multiplying by both a small and large dense matrix, to hit
# both cases in the kernel.
dense_t = np.array([[1] * 5, [2] * 5], dtype=np.float32)
expected_t = np.array([[0] * 5, [np.nan] * 5, [0] * 5], dtype=np.float32)
self.assertAllClose(
    expected_t, sparse_ops.sparse_tensor_dense_matmul(sparse_t, dense_t))
dense_t = np.array([[1] * 500, [2] * 500], dtype=np.float32)
expected_t = np.array([[0] * 500, [np.nan] * 500, [0] * 500],
                      dtype=np.float32)
self.assertAllClose(
    expected_t, sparse_ops.sparse_tensor_dense_matmul(sparse_t, dense_t))

# Repeat with adjoint_a, now the error is that the sparse index
# is OOO w.r.t. the output.  The GPU kernel can't do much here,
# so it just doesn't accumulate.

dense_t = np.array([[1] * 5, [2] * 5, [3] * 5], dtype=np.float32)
expected_t = np.array([[0] * 5, [0] * 5], dtype=np.float32)
self.assertAllClose(
    expected_t,
    sparse_ops.sparse_tensor_dense_matmul(
        sparse_t, dense_t, adjoint_a=True))

dense_t = np.array([[1] * 500, [2] * 500, [3] * 500], dtype=np.float32)
expected_t = np.array([[0] * 500, [0] * 500], dtype=np.float32)
self.assertAllClose(
    expected_t,
    sparse_ops.sparse_tensor_dense_matmul(
        sparse_t, dense_t, adjoint_a=True))
