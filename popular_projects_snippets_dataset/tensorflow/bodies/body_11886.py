# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
r"""Initialize a `LinearOperatorTridiag`.

    Args:
      diagonals: `Tensor` or list of `Tensor`s depending on `diagonals_format`.

        If `diagonals_format=sequence`, this is a list of three `Tensor`'s each
        with shape `[B1, ..., Bb, N]`, `b >= 0, N >= 0`, representing the
        superdiagonal, diagonal and subdiagonal in that order. Note the
        superdiagonal is padded with an element in the last position, and the
        subdiagonal is padded with an element in the front.

        If `diagonals_format=matrix` this is a `[B1, ... Bb, N, N]` shaped
        `Tensor` representing the full tridiagonal matrix.

        If `diagonals_format=compact` this is a `[B1, ... Bb, 3, N]` shaped
        `Tensor` with the second to last dimension indexing the
        superdiagonal, diagonal and subdiagonal in that order. Note the
        superdiagonal is padded with an element in the last position, and the
        subdiagonal is padded with an element in the front.

        In every case, these `Tensor`s are all floating dtype.
      diagonals_format: one of `matrix`, `sequence`, or `compact`. Default is
        `compact`.
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

    Raises:
      TypeError:  If `diag.dtype` is not an allowed type.
      ValueError:  If `diag.dtype` is real, and `is_self_adjoint` is not `True`.
    """
parameters = dict(
    diagonals=diagonals,
    diagonals_format=diagonals_format,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)

with ops.name_scope(name, values=[diagonals]):
    if diagonals_format not in _DIAGONAL_FORMATS:
        raise ValueError(
            f'Argument `diagonals_format` must be one of compact, matrix, or '
            f'sequence. Received : {diagonals_format}.')
    if diagonals_format == _SEQUENCE:
        self._diagonals = [linear_operator_util.convert_nonref_to_tensor(
            d, name='diag_{}'.format(i)) for i, d in enumerate(diagonals)]
        dtype = self._diagonals[0].dtype
    else:
        self._diagonals = linear_operator_util.convert_nonref_to_tensor(
            diagonals, name='diagonals')
        dtype = self._diagonals.dtype
    self._diagonals_format = diagonals_format

    super(LinearOperatorTridiag, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
