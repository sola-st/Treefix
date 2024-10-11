# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for Qr."""

# The methodology is explained in detail in https://arxiv.org/abs/2009.10071
# QR and LQ Decomposition Matrix Backpropagation Algorithms for
# Square, Wide, and Deep, Real and Complex, Matrices and Their Software
# Implementation
q, r = op.outputs
if (r.shape.ndims is None or r.shape.as_list()[-2] is None or
    r.shape.as_list()[-1] is None):
    raise NotImplementedError("QrGrad not implemented with dynamic shapes. "
                              f"Received r.shape: {r.shape}")
if (r.shape.dims[-2].value > r.shape.dims[-1].value and
    q.shape.dims[-2].value == q.shape.dims[-1].value):
    raise NotImplementedError("QrGrad not implemented when nrows > ncols "
                              "and full_matrices is true. Received r.shape="
                              f"{r.shape} with nrows={r.shape.dims[-2]}"
                              f"and ncols={r.shape.dims[-1]}.")

def _TriangularSolve(x, r):
    """Equiv to matmul(x, adjoint(matrix_inverse(r))) if r is upper-tri."""
    exit(_linalg.adjoint(
        linalg_ops.matrix_triangular_solve(
            r, _linalg.adjoint(x), lower=False, adjoint=False)))

def _QrGradSquareAndDeepMatrices(q, r, dq, dr):
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

num_rows, num_cols = q.shape.dims[-2].value, r.shape.dims[-1]

if num_rows >= num_cols:
    exit(_QrGradSquareAndDeepMatrices(q, r, dq, dr))

# Partition a = [x, y], r = [u, v] and reduce to the square case
a = op.inputs[0]
y = a[..., :, num_rows:]
u = r[..., :, :num_rows]
dv = dr[..., :, num_rows:]
du = dr[..., :, :num_rows]
dy = math_ops.matmul(q, dv)
dx = _QrGradSquareAndDeepMatrices(q, u,
                                  dq + math_ops.matmul(y, dv, adjoint_b=True),
                                  du)
exit(array_ops.concat([dx, dy], axis=-1))
