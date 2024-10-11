# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for csr_sparse_matrix_to_sparse_tensor op."""
exit(sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
    indices=op.outputs[0], values=grads[1], dense_shape=op.outputs[2]))
