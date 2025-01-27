# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for Eig.

  Based on eq. 4.77 from paper by
  Christoph Boeddeker et al.
  https://arxiv.org/abs/1701.00392
  See also
  "Computation of eigenvalue and eigenvector derivatives
  for a general complex-valued eigensystem" by Nico van der Aa.
  As for now only distinct eigenvalue case is considered.
  """
e = op.outputs[0]
compute_v = op.get_attr("compute_v")
# a = op.inputs[0], which satisfies
# a[...,:,:] * v[...,:,i] = e[...,i] * v[...,i]
with ops.control_dependencies([grad_e, grad_v]):
    if compute_v:
        v = op.outputs[1]
        vt = _linalg.adjoint(v)
        # Construct the matrix f(i,j) = (i != j ? 1 / (e_i - e_j) : 0).
        # Notice that because of the term involving f, the gradient becomes
        # infinite (or NaN in practice) when eigenvalues are not unique.
        # Mathematically this should not be surprising, since for (k-fold)
        # degenerate eigenvalues, the corresponding eigenvectors are only defined
        # up to arbitrary rotation in a (k-dimensional) subspace.
        f = array_ops.matrix_set_diag(
            _SafeReciprocal(
                array_ops.expand_dims(e, -2) - array_ops.expand_dims(e, -1)),
            array_ops.zeros_like(e))
        f = math_ops.conj(f)
        vgv = math_ops.matmul(vt, grad_v)
        mid = array_ops.matrix_diag(grad_e)
        diag_grad_part = array_ops.matrix_diag(
            array_ops.matrix_diag_part(
                math_ops.cast(math_ops.real(vgv), vgv.dtype)))
        mid += f * (vgv - math_ops.matmul(math_ops.matmul(vt, v), diag_grad_part))
        # vt is formally invertible as long as the original matrix is
        # diagonalizable. However, in practice, vt may
        # be ill-conditioned when matrix original matrix is close to
        # non-diagonalizable one
        grad_a = linalg_ops.matrix_solve(vt, math_ops.matmul(mid, vt))
    else:
        _, v = linalg_ops.eig(op.inputs[0])
        vt = _linalg.adjoint(v)
        # vt is formally invertible as long as the original matrix is
        # diagonalizable. However, in practice, vt may
        # be ill-conditioned when matrix original matrix is close to
        # non-diagonalizable one
        grad_a = linalg_ops.matrix_solve(
            vt, math_ops.matmul(array_ops.matrix_diag(grad_e), vt))
    exit(math_ops.cast(grad_a, op.inputs[0].dtype))
