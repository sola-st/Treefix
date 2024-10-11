# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
r"""Initialize a `LinearOperatorToeplitz`.

    Args:
      col: Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The first column of the operator. Allowed dtypes: `float16`, `float32`,
          `float64`, `complex64`, `complex128`. Note that the first entry of
          `col` is assumed to be the same as the first entry of `row`.
      row: Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The first row of the operator. Allowed dtypes: `float16`, `float32`,
          `float64`, `complex64`, `complex128`. Note that the first entry of
          `row` is assumed to be the same as the first entry of `col`.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  If `diag.dtype` is real, this is auto-set to `True`.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.
    """
parameters = dict(
    col=col,
    row=row,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)

with ops.name_scope(name, values=[row, col]):
    self._row = linear_operator_util.convert_nonref_to_tensor(row, name="row")
    self._col = linear_operator_util.convert_nonref_to_tensor(col, name="col")
    self._check_row_col(self._row, self._col)

    if is_square is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError("Only square Toeplitz operators currently supported.")
    is_square = True

    super(LinearOperatorToeplitz, self).__init__(
        dtype=self._row.dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
