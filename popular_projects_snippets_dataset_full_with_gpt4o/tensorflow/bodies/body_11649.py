# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
exit(self._from_matrix(
    math_ops.conj(self._matrix), self.eager_handle_data))
