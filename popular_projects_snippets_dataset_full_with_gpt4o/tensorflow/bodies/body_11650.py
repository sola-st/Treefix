# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Return the hermitian transpose of the matrix."""
exit(self._from_matrix(
    sm_ops.sparse_matrix_transpose(
        self._matrix, conjugate=True, type=self.dtype),
    self.eager_handle_data))
