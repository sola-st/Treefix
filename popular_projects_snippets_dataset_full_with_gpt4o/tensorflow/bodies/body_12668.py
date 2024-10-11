# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
r"""Computes Cholesky factorization of regularized gramian matrix.

  Below we will use the following notation for each pair of matrix and
  right-hand sides in the batch:

  `matrix`=\\(A \in \Re^{m \times n}\\),
  `output`=\\(C  \in \Re^{\min(m, n) \times \min(m,n)}\\),
  `l2_regularizer`=\\(\lambda\\).

  If `first_kind` is True, returns the Cholesky factorization \\(L\\) such that
  \\(L L^H =  A^H A + \lambda I\\).
  If `first_kind` is False, returns the Cholesky factorization \\(L\\) such that
  \\(L L^H =  A A^H + \lambda I\\).

  Args:
    matrix: `Tensor` of shape `[..., M, N]`.
    l2_regularizer: 0-D `double` `Tensor`. Ignored if `fast=False`.
    first_kind: bool. Controls what gramian matrix to factor.
  Returns:
    output: `Tensor` of shape `[..., min(M,N), min(M,N)]` whose inner-most 2
      dimensions contain the Cholesky factors \\(L\\) described above.
  """

gramian = math_ops.matmul(
    matrix, matrix, adjoint_a=first_kind, adjoint_b=not first_kind)
if isinstance(l2_regularizer, ops.Tensor) or l2_regularizer != 0:
    matrix_shape = array_ops.shape(matrix)
    batch_shape = matrix_shape[:-2]
    if first_kind:
        small_dim = matrix_shape[-1]
    else:
        small_dim = matrix_shape[-2]
    identity = eye(small_dim, batch_shape=batch_shape, dtype=matrix.dtype)
    small_dim_static = matrix.shape[-1 if first_kind else -2]
    identity.set_shape(
        matrix.shape[:-2].concatenate([small_dim_static, small_dim_static]))
    gramian += l2_regularizer * identity
exit(gen_linalg_ops.cholesky(gramian))
