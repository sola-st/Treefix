# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for sparse_matrix_add op."""
# input to sparse_matrix_add is (a, b, alpha, beta)
# with a, b CSR and alpha beta scalars.
# output is: alpha * a + beta * b

# d(a*A + b*B)/dA . grad = a * grad

# May have gotten the transposes wrong below.
# d(a*A + b*B)/da . grad = tr(A' . grad)

# For now, only implement gradients w.r.t. A and B.
# TODO(ebrevdo): Implement reduce_sum for SparseMatrix so that we
# can implement gradients w.r.t. a and b.
(a_csr, b_csr, alpha, beta) = op.inputs
exit((sparse_csr_matrix_ops.sparse_matrix_mul(
    _PruneCSRMatrix(grad, a_csr), alpha),
        sparse_csr_matrix_ops.sparse_matrix_mul(
            _PruneCSRMatrix(grad, b_csr), beta), None, None))
