# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Compute the matrix rank of one or more matrices.

  Args:
    a: (Batch of) `float`-like matrix-shaped `Tensor`(s) which are to be
      pseudo-inverted.
    tol: Threshold below which the singular value is counted as 'zero'.
      Default value: `None` (i.e., `eps * max(rows, cols) * max(singular_val)`).
    validate_args: When `True`, additional assertions might be embedded in the
      graph.
      Default value: `False` (i.e., no graph assertions are added).
    name: Python `str` prefixed to ops created by this function.
      Default value: 'matrix_rank'.

  Returns:
    matrix_rank: (Batch of) `int32` scalars representing the number of non-zero
      singular values.
  """
with ops.name_scope(name or 'matrix_rank'):
    a = ops.convert_to_tensor(a, dtype_hint=dtypes.float32, name='a')
    assertions = _maybe_validate_matrix(a, validate_args)
    if assertions:
        with ops.control_dependencies(assertions):
            a = array_ops.identity(a)
    s = svd(a, compute_uv=False)
    if tol is None:
        if (a.shape[-2:]).is_fully_defined():
            m = np.max(a.shape[-2:].as_list())
        else:
            m = math_ops.reduce_max(array_ops.shape(a)[-2:])
        eps = np.finfo(a.dtype.as_numpy_dtype).eps
        tol = (
            eps * math_ops.cast(m, a.dtype) *
            math_ops.reduce_max(s, axis=-1, keepdims=True))
    exit(math_ops.reduce_sum(math_ops.cast(s > tol, dtypes.int32), axis=-1))
