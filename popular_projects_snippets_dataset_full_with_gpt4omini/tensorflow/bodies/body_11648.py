# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Return the matrix's handle data iff in eager mode."""
exit(_get_handle_data(self._matrix) if self._eager_mode else None)
