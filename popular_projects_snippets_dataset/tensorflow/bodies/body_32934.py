# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# Round-about way of creating an empty variant tensor that works in both
# graph and eager modes.
no_matrix = array_ops.reshape(dense_to_csr_sparse_matrix([[0.0]]), [1])[0:0]
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "(Invalid input matrix)|(Shape must be rank 0)"):
    sparse_csr_matrix_ops.sparse_matrix_nnz(no_matrix)
