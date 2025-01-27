# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for dense_to_csr_sparse_matrix op."""
grad_values = (
    sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        grad, type=op.get_attr("T")))
# inputs to fw op were: params, indices.
exit((grad_values, None))
