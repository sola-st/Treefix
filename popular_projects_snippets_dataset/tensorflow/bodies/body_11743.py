# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
r"""Initialize a `LinearOperatorKronecker`.

    `LinearOperatorKronecker` is initialized with a list of operators
    `[op_1,...,op_J]`.

    Args:
      operators:  Iterable of `LinearOperator` objects, each with
        the same `dtype` and composable shape, representing the Kronecker
        factors.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix\
            #Extension_for_non_symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.  Default is the individual
        operators names joined with `_x_`.

    Raises:
      TypeError:  If all operators do not have the same `dtype`.
      ValueError:  If `operators` is empty.
    """
parameters = dict(
    operators=operators,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)

# Validate operators.
check_ops.assert_proper_iterable(operators)
operators = list(operators)
if not operators:
    raise ValueError(f"Argument `operators` must be a list of >=1 operators. "
                     f"Received: {operators}.")
self._operators = operators

# Validate dtype.
dtype = operators[0].dtype
for operator in operators:
    if operator.dtype != dtype:
        name_type = (str((o.name, o.dtype)) for o in operators)
        raise TypeError(
            f"Expected every operation in argument `operators` to have the "
            f"same dtype. Received {list(name_type)}.")

    # Auto-set and check hints.
    # A Kronecker product is invertible, if and only if all factors are
    # invertible.
if all(operator.is_non_singular for operator in operators):
    if is_non_singular is False:
        raise ValueError(
            f"The Kronecker product of non-singular operators is always "
            f"non-singular. Expected argument `is_non_singular` to be True. "
            f"Received: {is_non_singular}.")
    is_non_singular = True

if all(operator.is_self_adjoint for operator in operators):
    if is_self_adjoint is False:
        raise ValueError(
            f"The Kronecker product of self-adjoint operators is always "
            f"self-adjoint. Expected argument `is_self_adjoint` to be True. "
            f"Received: {is_self_adjoint}.")
    is_self_adjoint = True

# The eigenvalues of a Kronecker product are equal to the products of eigen
# values of the corresponding factors.
if all(operator.is_positive_definite for operator in operators):
    if is_positive_definite is False:
        raise ValueError(
            f"The Kronecker product of positive-definite operators is always "
            f"positive-definite. Expected argument `is_positive_definite` to "
            f"be True. Received: {is_positive_definite}.")
    is_positive_definite = True

if name is None:
    name = operators[0].name
    for operator in operators[1:]:
        name += "_x_" + operator.name
with ops.name_scope(name):
    super(LinearOperatorKronecker, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
