# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
sparsity = 0.1
sparsify = lambda m: m * (m > 1 - sparsity)

batch_size = 53
num_rows = 147
dense_shape = [batch_size, num_rows, num_rows]

dense_matrix = sparsify(np.random.uniform(size=dense_shape)).astype(
    np.float32)

# Create a "random" SPD matrix, by choosing each entry of A between
# 0 and 1 at the specified density, and computing 0.5(A + At) + n*I.
# This ensures diagonal dominance which implies positive-definiteness.
dense_matrix = (
    0.5 *
    (dense_matrix + array_ops.transpose(dense_matrix, perm=[0, 2, 1])) +
    num_rows * linalg_ops.eye(dense_shape[-1], batch_shape=[batch_size]))
# Compute the fill-in reducing permutation and use it to perform
# the Sparse Cholesky factorization.
sparse_matrix = dense_to_csr_sparse_matrix(dense_matrix)
ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(
    sparse_matrix)

cholesky_sparse_matrix = \
        sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
        sparse_matrix, ordering_amd, type=dtypes.float32)
dense_cholesky = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    cholesky_sparse_matrix, dtypes.float32)

# Compute L * Lh.
verification = test_util.matmul_without_tf32(
    dense_cholesky, array_ops.transpose(dense_cholesky, perm=[0, 2, 1]))
verification = twist_matrix(verification, ordering_amd)
verification_values = self.evaluate(verification)
self.assertAllClose(dense_matrix, verification_values, atol=1e-5, rtol=1e-5)
