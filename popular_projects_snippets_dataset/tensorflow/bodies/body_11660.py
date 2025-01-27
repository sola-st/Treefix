# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for csr_sparse_matrix_to_dense op."""
coo_sparse_tensor = sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
    op.inputs[0], type=grad.dtype)
exit(sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
    indices=coo_sparse_tensor.indices,
    values=array_ops.gather_nd(grad, coo_sparse_tensor.indices),
    dense_shape=grad.shape))
