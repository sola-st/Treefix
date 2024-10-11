# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_sparse_mat_mul_grad_test.py
# Skip invalid cases.
if (t_a_ and adj_a_) or (t_b_ and adj_b_):
    exit()
# Skip cases where we conjugate real matrices.
if dtype_ == np.float32 and (adj_a_ or adj_b_):
    exit()

def test_fn(self):
    self._testLargeBatchSparseMatrixSparseMatMulGrad(
        dtype_, t_a_, t_b_, adj_a_, adj_b_)

exit(test_fn)
