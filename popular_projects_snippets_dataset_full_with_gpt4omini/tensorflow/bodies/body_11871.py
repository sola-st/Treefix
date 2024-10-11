# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
r"""Initialize a `LinearOperatorPermutation`.

    Args:
      perm:  Shape `[B1,...,Bb, N]` Integer `Tensor` with `b >= 0`
        `N >= 0`. An integer vector that represents the permutation to apply.
        Note that this argument is same as `tf.transpose`. However, this
        permutation is applied on the rows, while the permutation in
        `tf.transpose` is applied on the dimensions of the `Tensor`. `perm`
        is required to have unique entries from `{0, 1, ... N-1}`.
      dtype: The `dtype` of arguments to this operator. Default: `float32`.
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
    perm=perm,
    dtype=dtype,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)

with ops.name_scope(name, values=[perm]):
    self._perm = linear_operator_util.convert_nonref_to_tensor(
        perm, name="perm")
    self._check_perm(self._perm)

    # Check and auto-set hints.
    if is_non_singular is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError(f"A Permutation operator is always non-singular. "
                         f"Expected argument `is_non_singular` to be True. "
                         f"Received: {is_non_singular}.")

    if is_square is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError(f"A Permutation operator is always square. "
                         f"Expected argument `is_square` to be True. "
                         f"Received: {is_square}.")
    is_square = True

    super(LinearOperatorPermutation, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
