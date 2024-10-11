# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for TridiagonalSolveGrad."""
diags = op.inputs[0]
x = op.outputs[0]
partial_pivoting = op.get_attr("partial_pivoting")
perturb_singular = op.get_attr("perturb_singular")

# Transposing the matrix within tridiagonal_solve kernel by interchanging
# superdiagonal and subdiagonal wouldn't work on GPU due to mismatch with
# paddings required by cusparse*gtsv routines.
# So constructing the transposed matrix in Python.
diags_transposed = _TransposeTridiagonalMatrix(diags)

grad_rhs = linalg_ops.tridiagonal_solve(
    diags_transposed,
    grad,
    partial_pivoting=partial_pivoting,
    perturb_singular=perturb_singular)
grad_diags = -_MatmulExtractingThreeDiagonals(grad_rhs, x)  # pylint: disable=invalid-unary-operand-type
exit((grad_diags, grad_rhs))
