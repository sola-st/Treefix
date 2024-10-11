# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_composition.py
r"""Initialize a `LinearOperatorComposition`.

    `LinearOperatorComposition` is initialized with a list of operators
    `[op_1,...,op_J]`.  For the `matmul` method to be well defined, the
    composition `op_i.matmul(op_{i+1}(x))` must be defined.  Other methods have
    similar constraints.

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
      name: A name for this `LinearOperator`.  Default is the individual
        operators names joined with `_o_`.

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
    name=name)

# Validate operators.
check_ops.assert_proper_iterable(operators)
operators = list(operators)
if not operators:
    raise ValueError(
        "Expected a non-empty list of operators. Found: %s" % operators)
self._operators = operators

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
    if is_non_singular is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError(
            "The composition of non-singular operators is always non-singular.")
    is_non_singular = True

if _composition_must_be_self_adjoint(operators):
    if is_self_adjoint is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError(
            "The composition was determined to be self-adjoint but user "
            "provided incorrect `False` hint.")
    is_self_adjoint = True

if linear_operator_util.is_aat_form(operators):
    if is_square is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError(
            "The composition was determined have the form "
            "A @ A.H, hence it must be square. The user "
            "provided an incorrect `False` hint.")
    is_square = True

if linear_operator_util.is_aat_form(operators) and is_non_singular:
    if is_positive_definite is False:  # pylint:disable=g-bool-id-comparison
        raise ValueError(
            "The composition was determined to be non-singular and have the "
            "form A @ A.H, hence it must be positive-definite. The user "
            "provided an incorrect `False` hint.")
    is_positive_definite = True

# Initialization.

if name is None:
    name = "_o_".join(operator.name for operator in operators)
with ops.name_scope(name):
    super(LinearOperatorComposition, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
