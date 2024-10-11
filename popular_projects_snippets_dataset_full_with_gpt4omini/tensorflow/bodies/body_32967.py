# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_dense_mat_mul_grad_test.py
if batched_inputs:
    a_shape = (3, 5, 11)
    b_shape = (3, 11, 13)
    transpose = lambda x: np.transpose(x, (0, 2, 1))
else:
    a_shape = (5, 11)
    b_shape = (11, 13)
    transpose = np.transpose

sparsify = lambda m: m * (m > 0)
a_mats_val = sparsify(
    np.random.randn(*a_shape) +
    1.j * np.random.randn(*a_shape)).astype(datatype)
if transpose_a or adjoint_a:
    a_mats_val = transpose(a_mats_val)
if adjoint_a:
    a_mats_val = np.conj(a_mats_val)
b_mats_val = (np.random.randn(*b_shape) +
              1.j * np.random.randn(*b_shape)).astype(datatype)
if transpose_b or adjoint_b:
    b_mats_val = transpose(b_mats_val)
if adjoint_b:
    b_mats_val = np.conj(b_mats_val)
with self.test_session():
    a_mats = ops.convert_to_tensor(a_mats_val, dtype=datatype)
    b_mats = ops.convert_to_tensor(b_mats_val, dtype=datatype)
    locs = array_ops.where(abs(a_mats_val) > 0)
    a_sm = sparse_csr_matrix_ops.dense_to_csr_sparse_matrix(a_mats, locs)
    c_mats = sparse_csr_matrix_ops.sparse_matrix_mat_mul(
        a_sm,
        b_mats,
        transpose_a=transpose_a,
        transpose_b=transpose_b,
        adjoint_a=adjoint_a,
        adjoint_b=adjoint_b,
        transpose_output=transpose_output,
        conjugate_output=conjugate_output)
    for [ten, val, nn] in [[a_mats, a_mats_val, "a"],
                           [b_mats, b_mats_val, "b"]]:
        tf_logging.info("Testing gradients for %s" % nn)
        theoretical, numerical = gradient_checker.compute_gradient(
            ten,
            ten.get_shape().as_list(),
            c_mats,
            c_mats.get_shape().as_list(),
            x_init_value=val,
            delta=1e-3)
        self.assertAllClose(theoretical, numerical, atol=1e-3, rtol=1e-3)
