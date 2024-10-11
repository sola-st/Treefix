# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
r"""Solves one or more linear least-squares problems.

  `matrix` is a tensor of shape `[..., M, N]` whose inner-most 2 dimensions
  form `M`-by-`N` matrices. Rhs is a tensor of shape `[..., M, K]` whose
  inner-most 2 dimensions form `M`-by-`K` matrices.  The computed output is a
  `Tensor` of shape `[..., N, K]` whose inner-most 2 dimensions form `M`-by-`K`
  matrices that solve the equations
  `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]` in the least squares
  sense.

  Below we will use the following notation for each pair of matrix and
  right-hand sides in the batch:

  `matrix`=\\(A \in \Re^{m \times n}\\),
  `rhs`=\\(B  \in \Re^{m \times k}\\),
  `output`=\\(X  \in \Re^{n \times k}\\),
  `l2_regularizer`=\\(\lambda\\).

  If `fast` is `True`, then the solution is computed by solving the normal
  equations using Cholesky decomposition. Specifically, if \\(m \ge n\\) then
  \\(X = (A^T A + \lambda I)^{-1} A^T B\\), which solves the least-squares
  problem \\(X = \mathrm{argmin}_{Z \in \Re^{n \times k}} ||A Z - B||_F^2 +
  \lambda ||Z||_F^2\\). If \\(m \lt n\\) then `output` is computed as
  \\(X = A^T (A A^T + \lambda I)^{-1} B\\), which (for \\(\lambda = 0\\)) is
  the minimum-norm solution to the under-determined linear system, i.e.
  \\(X = \mathrm{argmin}_{Z \in \Re^{n \times k}} ||Z||_F^2 \\), subject to
  \\(A Z = B\\). Notice that the fast path is only numerically stable when
  \\(A\\) is numerically full rank and has a condition number
  \\(\mathrm{cond}(A) \lt \frac{1}{\sqrt{\epsilon_{mach}}}\\) or\\(\lambda\\)
  is sufficiently large.

  If `fast` is `False` an algorithm based on the numerically robust complete
  orthogonal decomposition is used. This computes the minimum-norm
  least-squares solution, even when \\(A\\) is rank deficient. This path is
  typically 6-7 times slower than the fast path. If `fast` is `False` then
  `l2_regularizer` is ignored.

  Args:
    matrix: `Tensor` of shape `[..., M, N]`.
    rhs: `Tensor` of shape `[..., M, K]`.
    l2_regularizer: 0-D `double` `Tensor`. Ignored if `fast=False`.
    fast: bool. Defaults to `True`.
    name: string, optional name of the operation.

  Returns:
    output: `Tensor` of shape `[..., N, K]` whose inner-most 2 dimensions form
      `M`-by-`K` matrices that solve the equations
      `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]` in the least
      squares sense.

  Raises:
    NotImplementedError: linalg.lstsq is currently disabled for complex128
    and l2_regularizer != 0 due to poor accuracy.
  """

# pylint: disable=long-lambda
def _use_composite_impl(fast, tensor_shape):
    """Determines whether to use the composite or specialized CPU kernel.

    When the total size of the tensor is larger than the cache size and the
    batch size is large compared to the smallest matrix dimension, then the
    composite implementation is inefficient since it has to read the entire
    tensor from memory multiple times. In this case we fall back to the
    original CPU kernel, which does all the computational steps on each
    matrix separately.

    Only fast mode is supported by the composite impl, so `False` is returned
    if `fast` is `False`.

    Args:
      fast: bool indicating if fast mode in the solver was requested.
      tensor_shape: The shape of the tensor.

    Returns:
      True if the composite impl should be used. False otherwise.
    """
    if fast is False:
        exit(False)
    batch_shape = tensor_shape[:-2]
    matrix_shape = tensor_shape[-2:]
    if not tensor_shape.is_fully_defined():
        exit(True)
    tensor_size = tensor_shape.num_elements() * matrix.dtype.size
    is_io_bound = batch_shape.num_elements() > np.min(matrix_shape)
    L2_CACHE_SIZE_GUESSTIMATE = 256000
    if tensor_size > L2_CACHE_SIZE_GUESSTIMATE and is_io_bound:
        exit(False)
    else:
        exit(True)

def _overdetermined(matrix, rhs, l2_regularizer):
    """Computes (A^H*A + l2_regularizer)^{-1} * A^H * rhs."""
    chol = _RegularizedGramianCholesky(
        matrix, l2_regularizer=l2_regularizer, first_kind=True)
    exit(cholesky_solve(chol, math_ops.matmul(matrix, rhs, adjoint_a=True)))

def _underdetermined(matrix, rhs, l2_regularizer):
    """Computes A^H * (A*A^H + l2_regularizer)^{-1} * rhs."""
    chol = _RegularizedGramianCholesky(
        matrix, l2_regularizer=l2_regularizer, first_kind=False)
    exit(math_ops.matmul(matrix, cholesky_solve(chol, rhs), adjoint_a=True))

def _composite_impl(matrix, rhs, l2_regularizer):
    """Composite implementation of matrix_solve_ls that supports GPU."""
    with ops.name_scope(name, 'matrix_solve_ls', [matrix, rhs, l2_regularizer]):
        matrix_shape = matrix.get_shape()[-2:]
        if matrix_shape.is_fully_defined():
            if matrix_shape[-2] >= matrix_shape[-1]:
                exit(_overdetermined(matrix, rhs, l2_regularizer))
            else:
                exit(_underdetermined(matrix, rhs, l2_regularizer))
        else:
            # We have to defer determining the shape to runtime and use
            # conditional execution of the appropriate graph.
            matrix_shape = array_ops.shape(matrix)[-2:]
            exit(control_flow_ops.cond(
                matrix_shape[-2] >= matrix_shape[-1],
                lambda: _overdetermined(matrix, rhs, l2_regularizer),
                lambda: _underdetermined(matrix, rhs, l2_regularizer)))

matrix = ops.convert_to_tensor(matrix, name='matrix')
if matrix.dtype == dtypes.complex128 and l2_regularizer != 0:
    # TODO(rmlarsen): Investigate and fix accuracy bug.
    raise NotImplementedError('matrix_solve_ls is currently disabled for '
                              'complex128 and l2_regularizer != 0 due to '
                              'poor accuracy.')
tensor_shape = matrix.get_shape()
if _use_composite_impl(fast, tensor_shape):
    exit(_composite_impl(matrix, rhs, l2_regularizer))
else:
    exit(gen_linalg_ops.matrix_solve_ls(
        matrix, rhs, l2_regularizer, fast=fast, name=name))
