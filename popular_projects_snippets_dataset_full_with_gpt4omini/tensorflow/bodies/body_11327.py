# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_inversion.py
r"""Initialize a `LinearOperatorInversion`.

    `LinearOperatorInversion` is initialized with an operator `A`.  The `solve`
    and `matmul` methods are effectively swapped.  E.g.

    ```
    A = MyLinearOperator(...)
    B = LinearOperatorInversion(A)
    x = [....]  # a vector

    assert A.matvec(x) == B.solvevec(x)
    ```

    Args:
      operator: `LinearOperator` object. If `operator.is_non_singular == False`,
        an exception is raised.  We do allow `operator.is_non_singular == None`,
        in which case this operator will have `is_non_singular == None`.
        Similarly for `is_self_adjoint` and `is_positive_definite`.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`. Default is `operator.name +
        "_inv"`.

    Raises:
      ValueError:  If `operator.is_non_singular` is False.
    """
parameters = dict(
    operator=operator,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)

self._operator = operator

# Auto-set and check hints.
if operator.is_non_singular is False or is_non_singular is False:
    raise ValueError(
        f"Argument `is_non_singular` or argument `operator` must have "
        f"supplied hint `is_non_singular` equal to `True` or `None`. "
        f"Found `operator.is_non_singular`: {operator.is_non_singular}, "
        f"`is_non_singular`: {is_non_singular}.")
if operator.is_square is False or is_square is False:
    raise ValueError(
        f"Argument `is_square` or argument `operator` must have supplied "
        f"hint `is_square` equal to `True` or `None`. Found "
        f"`operator.is_square`: {operator.is_square}, "
        f"`is_square`: {is_square}.")

# The congruency of is_non_singular and is_self_adjoint was checked in the
# base operator.  Other hints are, in this special case of inversion, ones
# that must be the same for base/derived operator.
combine_hint = (
    linear_operator_util.use_operator_or_provided_hint_unless_contradicting)

is_square = combine_hint(
    operator, "is_square", is_square,
    "An operator is square if and only if its inverse is square.")

is_non_singular = combine_hint(
    operator, "is_non_singular", is_non_singular,
    "An operator is non-singular if and only if its inverse is "
    "non-singular.")

is_self_adjoint = combine_hint(
    operator, "is_self_adjoint", is_self_adjoint,
    "An operator is self-adjoint if and only if its inverse is "
    "self-adjoint.")

is_positive_definite = combine_hint(
    operator, "is_positive_definite", is_positive_definite,
    "An operator is positive-definite if and only if its inverse is "
    "positive-definite.")

# Initialization.
if name is None:
    name = operator.name + "_inv"
with ops.name_scope(name):
    super(LinearOperatorInversion, self).__init__(
        dtype=operator.dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
