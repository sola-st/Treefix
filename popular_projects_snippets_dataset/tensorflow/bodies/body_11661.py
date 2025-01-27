# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for sparse_tensor_to_csr_sparse_matrix op."""
grad_values = sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
    grad, type=op.get_attr("T")).values
exit((None, grad_values, None))
