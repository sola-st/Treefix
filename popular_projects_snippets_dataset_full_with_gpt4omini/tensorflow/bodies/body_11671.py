# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
"""Gradient for sparse_matrix_sparse_mat_mul op."""
t_a = op.get_attr("transpose_a")
t_b = op.get_attr("transpose_b")
adj_a = op.get_attr("adjoint_a")
adj_b = op.get_attr("adjoint_b")
dtype = op.get_attr("type")

# input to sparse_matrix_sparse_mat_mul is (A, B) with CSR A and B.
# Output is CSR:
#   C = opA(A) . opB(B)
# where opA = transpose if transpose_a = True else identity
# and   opB = transpose if transpose_b = True else identity
a = op.inputs[0]
b = op.inputs[1]
conj = math_ops.conj
matmul = sparse_csr_matrix_ops.sparse_matrix_sparse_mat_mul
if not t_a and not t_b:
    if not adj_a:
        if not adj_b:
            grad_a = matmul(grad, b, adjoint_b=True, type=dtype)
            grad_b = matmul(a, grad, adjoint_a=True, type=dtype)
        else:
            grad_a = matmul(grad, b, type=dtype)
            grad_b = matmul(grad, a, adjoint_a=True, type=dtype)
    else:
        if not adj_b:
            grad_a = matmul(b, grad, adjoint_b=True, type=dtype)
            grad_b = matmul(a, grad, type=dtype)
        else:
            grad_a = matmul(b, grad, adjoint_a=True, adjoint_b=True, type=dtype)
            grad_b = matmul(grad, a, adjoint_a=True, adjoint_b=True, type=dtype)
elif not adj_a and not adj_b:
    if not t_a and t_b:
        grad_a = matmul(grad, conj(b), type=dtype)
        grad_b = matmul(grad, conj(a), transpose_a=True, type=dtype)
    elif t_a and not t_b:
        grad_a = matmul(conj(b), grad, transpose_b=True, type=dtype)
        grad_b = matmul(conj(a), grad, type=dtype)
    else:
        grad_a = matmul(b, grad, adjoint_a=True, transpose_b=True, type=dtype)
        grad_b = matmul(grad, a, transpose_a=True, adjoint_b=True, type=dtype)
elif adj_a and t_b:
    grad_a = matmul(b, grad, transpose_a=True, adjoint_b=True, type=dtype)
    grad_b = matmul(grad, a, transpose_a=True, transpose_b=True, type=dtype)
elif t_a and adj_b:
    grad_a = matmul(b, grad, transpose_a=True, transpose_b=True, type=dtype)
    grad_b = matmul(grad, a, adjoint_a=True, transpose_b=True, type=dtype)

# TODO(tabakg): There should be a C++ function for sparse-sparse
# multiplication with pre-determined indices, instead of pruning after the
# multiplication.
exit((_PruneCSRMatrix(grad_a, a), _PruneCSRMatrix(grad_b, b)))
