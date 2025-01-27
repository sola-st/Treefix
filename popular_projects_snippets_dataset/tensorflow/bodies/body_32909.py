# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
sparsify = lambda m: m * (m > 0)
transpose_a, transpose_b = transpose
adjoint_a, adjoint_b = adjoint
if (transpose_a and adjoint_a) or (transpose_b and adjoint_b):
    exit()
# Make copies so we don't update the lists inside the decorator arguments.
a_dense_shape = shapes[0][:]
b_dense_shape = shapes[1][:]
if transpose_a or adjoint_a:
    _swap(a_dense_shape, -2, -1)
if transpose_b or adjoint_b:
    _swap(b_dense_shape, -2, -1)
a_mats = sparsify((np.random.randn(*a_dense_shape) +
                   1.j * np.random.randn(*a_dense_shape))).astype(dtype)
b_mats = (np.random.randn(*b_dense_shape) +
          1.j * np.random.randn(*b_dense_shape)).astype(dtype)
tf_logging.info(
    "testLargeBatchSparseMatrixMatMul transpose_a %s transpose_b "
    "%s adjoint_a %s adjoint_b %s" %
    (transpose_a, transpose_b, adjoint_a, adjoint_b))
a_sm = dense_to_csr_sparse_matrix(a_mats)
c_t = sparse_csr_matrix_ops.sparse_matrix_mat_mul(
    a_sm,
    b_mats,
    transpose_output=False,
    conjugate_output=False,
    transpose_a=transpose_a,
    transpose_b=transpose_b,
    adjoint_a=adjoint_a,
    adjoint_b=adjoint_b)
c_dense_t = test_util.matmul_without_tf32(
    a_mats,
    b_mats,
    transpose_a=transpose_a,
    transpose_b=transpose_b,
    adjoint_a=adjoint_a,
    adjoint_b=adjoint_b)
self.assertAllEqual(c_dense_t.shape, c_t.shape)
c_t_value, c_dense_t_value = self.evaluate((c_t, c_dense_t))

self.assertAllClose(c_t_value, c_dense_t_value, rtol=1e-6, atol=2e-5)
