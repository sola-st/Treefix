# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for sparse_matrix_softmax op."""
softmax = op.outputs[0]
exit(sparse_csr_matrix_ops.sparse_matrix_softmax_grad(
    softmax, grad_softmax, type=op.get_attr("type")))
