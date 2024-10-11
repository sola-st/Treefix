# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
r"""Initialize a `LinearOperatorDiag`.

    Args:
      diag:  Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The diagonal of the operator.  Allowed dtypes: `float16`, `float32`,
          `float64`, `complex64`, `complex128`.
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
    diag=diag,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)

with ops.name_scope(name, values=[diag]):
    self._diag = linear_operator_util.convert_nonref_to_tensor(
        diag, name="diag")
    self._check_diag(self._diag)

    # Check and auto-set hints.
    if not self._diag.dtype.is_complex:
        if is_self_adjoint is False:
            raise ValueError("A real diagonal operator is always self adjoint.")
        else:
            is_self_adjoint = True

    if is_square is False:
        raise ValueError("Only square diagonal operators currently supported.")
    is_square = True

    super(LinearOperatorDiag, self).__init__(
        dtype=self._diag.dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
