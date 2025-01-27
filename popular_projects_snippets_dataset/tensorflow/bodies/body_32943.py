# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_sparse_mat_mul_grad_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
a_mats_val = sparsify(
    np.random.randn(3, 5, 11) +
    1.j * np.random.randn(3, 5, 11)).astype(datatype)
if transpose_a or adjoint_a:
    a_mats_val = np.transpose(a_mats_val, (0, 2, 1))
if adjoint_a:
    a_mats_val = np.conj(a_mats_val)
b_mats_val = sparsify(
    np.random.randn(3, 11, 13) +
    1.j * np.random.randn(3, 11, 13)).astype(datatype)
if transpose_b or adjoint_b:
    b_mats_val = np.transpose(b_mats_val, (0, 2, 1))
if adjoint_b:
    b_mats_val = np.conj(b_mats_val)
with self.test_session():
    a_mats, a_sm = dense_and_sparse_from_vals(a_mats_val, datatype)
    b_mats, b_sm = dense_and_sparse_from_vals(b_mats_val, datatype)
    c_sm = sparse_csr_matrix_ops.sparse_matrix_sparse_mat_mul(
        a_sm,
        b_sm,
        transpose_a=transpose_a,
        transpose_b=transpose_b,
        adjoint_a=adjoint_a,
        adjoint_b=adjoint_b,
        type=datatype)
    c_dense = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        c_sm, type=datatype)
    for ten, val, nn in [[a_mats, a_mats_val, "a"], [b_mats, b_mats_val,
                                                     "b"]]:
        tf_logging.info("Testing gradients for %s" % nn)
        theoretical, numerical = gradient_checker.compute_gradient(
            ten,
            ten.get_shape().as_list(),
            c_dense,
            c_dense.get_shape().as_list(),
            x_init_value=val,
            delta=1e-3)
        self.assertAllClose(theoretical, numerical, atol=1e-3, rtol=1e-3)
