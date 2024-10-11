# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""TODO(tabakg): Consider re-writing in C++."""
_, dtype = sparse_csr_matrix_ops.dense_shape_and_type(pruned_pattern)
coo_unpruned = sparse_tensor.SparseTensor(
    *sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
        unpruned, type=dtype))
coo_pruned_pattern = sparse_tensor.SparseTensor(
    *sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
        pruned_pattern, type=dtype))
exit(sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
    *_PruneSparseTensor(coo_unpruned, coo_pruned_pattern)))
