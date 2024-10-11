# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
r"""Initialize a `LinearOperatorHouseholder`.

    Args:
      reflection_axis:  Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The vector defining the hyperplane to reflect about.
        Allowed dtypes: `float16`, `float32`, `float64`, `complex64`,
        `complex128`.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  This is autoset to true
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
        This is autoset to false.
      is_square:  Expect that this operator acts like square [batch] matrices.
        This is autoset to true.
      name: A name for this `LinearOperator`.

    Raises:
      ValueError:  `is_self_adjoint` is not `True`, `is_positive_definite` is
        not `False` or `is_square` is not `True`.
    """
parameters = dict(
    reflection_axis=reflection_axis,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)

with ops.name_scope(name, values=[reflection_axis]):
    self._reflection_axis = linear_operator_util.convert_nonref_to_tensor(
        reflection_axis, name="reflection_axis")
    self._check_reflection_axis(self._reflection_axis)

    # Check and auto-set hints.
    if is_self_adjoint is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError("A Householder operator is always self adjoint.")
    else:
        is_self_adjoint = True

    if is_positive_definite is True:  # pylint:disable=g-bool-id-comparison
        raise ValueError(
            "A Householder operator is always non-positive definite.")
    else:
        is_positive_definite = False

    if is_square is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError("A Householder operator is always square.")
    is_square = True

    super(LinearOperatorHouseholder, self).__init__(
        dtype=self._reflection_axis.dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
