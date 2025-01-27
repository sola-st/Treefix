# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for sparse_matrix_transpose op."""
exit(sparse_csr_matrix_ops.sparse_matrix_transpose(
    grad, type=op.get_attr("type"), conjugate=op.get_attr("conjugate")))
