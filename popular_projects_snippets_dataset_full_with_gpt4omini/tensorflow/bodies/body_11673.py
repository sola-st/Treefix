# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
r"""Initialize a `LinearOperatorBlockLowerTriangular`.

    `LinearOperatorBlockLowerTriangular` is initialized with a list of lists of
    operators `[[op_0], [op_1, op_2], [op_3, op_4, op_5],...]`.

    Args:
      operators:  Iterable of iterables of `LinearOperator` objects, each with
        the same `dtype`. Each element of `operators` corresponds to a row-
        partition, in top-to-bottom order. The operators in each row-partition
        are filled in left-to-right. For example,
        `operators = [[op_0], [op_1, op_2], [op_3, op_4, op_5]]` creates a
        `LinearOperatorBlockLowerTriangular` with full block structure
        `[[op_0, 0, 0], [op_1, op_2, 0], [op_3, op_4, op_5]]`. The number of
        operators in the `i`th row must be equal to `i`, such that each operator
        falls on or below the diagonal of the blockwise structure.
        `LinearOperator`s that fall on the diagonal (the last elements of each
        row) must be square. The other `LinearOperator`s must have domain
        dimension equal to the domain dimension of the `LinearOperator`s in the
        same column-partition, and range dimension equal to the range dimension
        of the `LinearOperator`s in the same row-partition.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
        This will raise a `ValueError` if set to `False`.
      name: A name for this `LinearOperator`.

    Raises:
      TypeError:  If all operators do not have the same `dtype`.
      ValueError:  If `operators` is empty, contains an erroneous number of
        elements, or contains operators with incompatible shapes.
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
for row in operators:
    check_ops.assert_proper_iterable(row)
operators = [list(row) for row in operators]

if not operators:
    raise ValueError(f"Argument `operators` must be a list of >=1 operators. "
                     f"Received: {operators}.")
self._operators = operators
self._diagonal_operators = [row[-1] for row in operators]

dtype = operators[0][0].dtype
self._validate_dtype(dtype)
is_non_singular = self._validate_non_singular(is_non_singular)
self._validate_num_operators()
self._validate_operator_dimensions()
is_square = self._validate_square(is_square)
with ops.name_scope(name):
    super(LinearOperatorBlockLowerTriangular, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
