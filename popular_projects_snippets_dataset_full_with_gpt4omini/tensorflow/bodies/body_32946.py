# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_grad_test.py
dense_t = ops.convert_to_tensor(dense)
locs = array_ops.where(math_ops.abs(dense_t) > 0)
exit(sparse_csr_matrix_ops.dense_to_csr_sparse_matrix(dense_t, locs))
