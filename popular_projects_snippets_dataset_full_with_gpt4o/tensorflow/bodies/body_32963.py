# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape_a = [5, 13, 7] if transpose_a or adjoint_a else [5, 7, 13]
dense_shape_b = [5, 15, 13] if transpose_b or adjoint_b else [5, 13, 15]
dtypes_to_test = [np.float32, np.complex64]
for dtype in dtypes_to_test:
    a_mats = (np.random.randn(*dense_shape_a) +
              1.j * np.random.randn(*dense_shape_a)).astype(dtype)
    b_mats = sparsify((np.random.randn(*dense_shape_b) +
                       1.j * np.random.randn(*dense_shape_b))).astype(dtype)
    b_sm = sparse_csr_matrix_ops.CSRSparseMatrix(b_mats)
    c_dense = test_util.matmul_without_tf32(
        a_mats,
        b_mats,
        transpose_a=transpose_a,
        transpose_b=transpose_b,
        adjoint_a=adjoint_a,
        adjoint_b=adjoint_b)
    c_sm_dense = sparse_csr_matrix_ops.matmul(
        a_mats,
        b_sm,
        transpose_a=transpose_a,
        transpose_b=transpose_b,
        adjoint_a=adjoint_a,
        adjoint_b=adjoint_b)
    c_dense, c_sm_dense = self.evaluate([c_dense, c_sm_dense])
    self.assertAllClose(c_dense, c_sm_dense)
