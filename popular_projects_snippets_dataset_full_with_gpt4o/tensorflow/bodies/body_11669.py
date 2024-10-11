# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
exit(_PrunedDenseMatrixMultiplication(
    x,
    y,
    indices=sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
        a, type=x.dtype).indices,
    **kwargs))
