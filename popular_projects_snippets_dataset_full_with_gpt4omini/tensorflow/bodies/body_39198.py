# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
# TODO(b/169813429): Make GPU kernel return nice errors too.
indices = np.array([[1, 10]]).astype(np.int64)
values = np.array([10]).astype(np.float32)
shape = [3, 2]
sparse_t = sparse_tensor.SparseTensor(indices, values, shape)

# Test multiplying by both a small and large dense matrix, to hit
# both cases in the kernel.
dense_t = np.array([[1] * 5, [2] * 5], dtype=np.float32)
with self.assertRaisesOpError("k .10. from index.0,1. out of bounds .>=2."):
    self.evaluate(sparse_ops.sparse_tensor_dense_matmul(sparse_t, dense_t))
dense_t = np.array([[1] * 500, [2] * 500], dtype=np.float32)
with self.assertRaisesOpError("k .10. from index.0,1. out of bounds .>=2."):
    self.evaluate(sparse_ops.sparse_tensor_dense_matmul(sparse_t, dense_t))

# Repeat with adjoint_a, to get a different error.
dense_t = np.array([[1] * 5, [2] * 5, [3] * 5], dtype=np.float32)
with self.assertRaisesOpError("m .10. from index.0,1. out of bounds .>=2."):
    self.evaluate(
        sparse_ops.sparse_tensor_dense_matmul(
            sparse_t, dense_t, adjoint_a=True))
dense_t = np.array([[1] * 500, [2] * 500, [3] * 500], dtype=np.float32)
with self.assertRaisesOpError("m .10. from index.0,1. out of bounds .>=2."):
    self.evaluate(
        sparse_ops.sparse_tensor_dense_matmul(
            sparse_t, dense_t, adjoint_a=True))
