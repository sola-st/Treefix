# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_sparse_mat_mul_grad_test.py
locs = array_ops.where(math_ops.abs(vals) > 0)
dense_t = ops.convert_to_tensor(vals, dtype=datatype)
exit((dense_t,
        sparse_csr_matrix_ops.dense_to_csr_sparse_matrix(dense_t, locs)))
