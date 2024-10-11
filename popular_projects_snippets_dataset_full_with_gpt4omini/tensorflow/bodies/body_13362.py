# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for matrix orders num_rows >= num_cols
    and full_matrices is false.
    """
qdq = math_ops.matmul(q, dq, adjoint_a=True)
qdq_ = qdq - _linalg.adjoint(qdq)
rdr = math_ops.matmul(r, dr, adjoint_b=True)
rdr_ = rdr - _linalg.adjoint(rdr)
tril = array_ops.matrix_band_part(qdq_ + rdr_, -1, 0)

grad_a = math_ops.matmul(q, dr + _TriangularSolve(tril, r))
grad_b = _TriangularSolve(dq - math_ops.matmul(q, qdq), r)
ret = grad_a + grad_b

if q.dtype.is_complex:
    # need to add a correction to the gradient formula for complex case
    m = rdr - _linalg.adjoint(qdq)
    eyem = _linalg.set_diag(array_ops.zeros_like(m), _linalg.diag_part(m))
    correction = eyem - math_ops.cast(math_ops.real(eyem), q.dtype)
    ret = ret + _TriangularSolve(
        math_ops.matmul(q, _linalg.adjoint(correction)), r)

exit(ret)
