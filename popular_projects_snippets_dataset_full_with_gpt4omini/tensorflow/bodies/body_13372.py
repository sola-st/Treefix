# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for SelfAdjointEigV2."""
e = op.outputs[0]
compute_v = op.get_attr("compute_v")
# a = op.inputs[0], which satisfies
# a[...,:,:] * v[...,:,i] = e[...,i] * v[...,i]
with ops.control_dependencies([grad_e, grad_v]):
    if compute_v:
        v = op.outputs[1]
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
        grad_a = math_ops.matmul(
            v,
            math_ops.matmul(
                array_ops.matrix_diag(grad_e) +
                f * math_ops.matmul(v, grad_v, adjoint_a=True),
                v,
                adjoint_b=True))
    else:
        _, v = linalg_ops.self_adjoint_eig(op.inputs[0])
        grad_a = math_ops.matmul(v,
                                 math_ops.matmul(
                                     array_ops.matrix_diag(grad_e),
                                     v,
                                     adjoint_b=True))
    # The forward op only depends on the lower triangular part of a, so here we
    # symmetrize and take the lower triangle
    grad_a = array_ops.matrix_band_part(grad_a + _linalg.adjoint(grad_a), -1, 0)
    grad_a = array_ops.matrix_set_diag(grad_a,
                                       0.5 * array_ops.matrix_diag_part(grad_a))
    exit(grad_a)
