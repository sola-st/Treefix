# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
r"""Initialize a `LinearOperatorBlockDiag`.

    `LinearOperatorBlockDiag` is initialized with a list of operators
    `[op_1,...,op_J]`.

    Args:
      operators:  Iterable of `LinearOperator` objects, each with
        the same `dtype` and composable shape.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
        This is true by default, and will raise a `ValueError` otherwise.
      name: A name for this `LinearOperator`.  Default is the individual
        operators names joined with `_o_`.

    Raises:
      TypeError:  If all operators do not have the same `dtype`.
      ValueError:  If `operators` is empty or are non-square.
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
    raise ValueError(
        "Expected a non-empty list of operators. Found: %s" % operators)
self._operators = operators

# Define diagonal operators, for functions that are shared across blockwise
# `LinearOperator` types.
self._diagonal_operators = operators

# Validate dtype.
dtype = operators[0].dtype
for operator in operators:
    if operator.dtype != dtype:
        name_type = (str((o.name, o.dtype)) for o in operators)
        raise TypeError(
            "Expected all operators to have the same dtype.  Found %s"
            % "   ".join(name_type))

    # Auto-set and check hints.
if all(operator.is_non_singular for operator in operators):
    if is_non_singular is False:
        raise ValueError(
            "The direct sum of non-singular operators is always non-singular.")
    is_non_singular = True

if all(operator.is_self_adjoint for operator in operators):
    if is_self_adjoint is False:
        raise ValueError(
            "The direct sum of self-adjoint operators is always self-adjoint.")
    is_self_adjoint = True

if all(operator.is_positive_definite for operator in operators):
    if is_positive_definite is False:
        raise ValueError(
            "The direct sum of positive definite operators is always "
            "positive definite.")
    is_positive_definite = True

if name is None:
    # Using ds to mean direct sum.
    name = "_ds_".join(operator.name for operator in operators)
with ops.name_scope(name):
    super(LinearOperatorBlockDiag, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
