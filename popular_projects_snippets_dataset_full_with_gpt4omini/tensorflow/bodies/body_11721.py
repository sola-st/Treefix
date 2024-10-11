# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_adjoint.py
r"""Initialize a `LinearOperatorAdjoint`.

    `LinearOperatorAdjoint` is initialized with an operator `A`.  The `solve`
    and `matmul` methods  effectively flip the `adjoint` argument.  E.g.

    ```
    A = MyLinearOperator(...)
    B = LinearOperatorAdjoint(A)
    x = [....]  # a vector

    assert A.matvec(x, adjoint=True) == B.matvec(x, adjoint=False)
    ```

    Args:
      operator: `LinearOperator` object.
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
        "_adjoint"`.

    Raises:
      ValueError:  If `operator.is_non_singular` is False.
    """
parameters = dict(
    operator=operator,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name,
)

self._operator = operator

# The congruency of is_non_singular and is_self_adjoint was checked in the
# base operator.
combine_hint = (
    linear_operator_util.use_operator_or_provided_hint_unless_contradicting)

is_square = combine_hint(
    operator, "is_square", is_square,
    "An operator is square if and only if its adjoint is square.")

is_non_singular = combine_hint(
    operator, "is_non_singular", is_non_singular,
    "An operator is non-singular if and only if its adjoint is "
    "non-singular.")

is_self_adjoint = combine_hint(
    operator, "is_self_adjoint", is_self_adjoint,
    "An operator is self-adjoint if and only if its adjoint is "
    "self-adjoint.")

is_positive_definite = combine_hint(
    operator, "is_positive_definite", is_positive_definite,
    "An operator is positive-definite if and only if its adjoint is "
    "positive-definite.")

# Initialization.
if name is None:
    name = operator.name + "_adjoint"
with ops.name_scope(name):
    super(LinearOperatorAdjoint, self).__init__(
        dtype=operator.dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
