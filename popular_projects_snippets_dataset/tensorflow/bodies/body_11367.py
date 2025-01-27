# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
r"""Initialize a `LinearOperatorScaledIdentity`.

    The `LinearOperatorScaledIdentity` is initialized with `num_rows`, which
    determines the size of each identity matrix, and a `multiplier`,
    which defines `dtype`, batch shape, and scale of each matrix.

    This operator is able to broadcast the leading (batch) dimensions.

    Args:
      num_rows:  Scalar non-negative integer `Tensor`.  Number of rows in the
        corresponding identity matrix.
      multiplier:  `Tensor` of shape `[B1,...,Bb]`, or `[]` (a scalar).
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      assert_proper_shapes:  Python `bool`.  If `False`, only perform static
        checks that initialization and method arguments have proper shape.
        If `True`, and static checks are inconclusive, add asserts to the graph.
      name: A name for this `LinearOperator`

    Raises:
      ValueError:  If `num_rows` is determined statically to be non-scalar, or
        negative.
    """
parameters = dict(
    num_rows=num_rows,
    multiplier=multiplier,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    assert_proper_shapes=assert_proper_shapes,
    name=name)

self._assert_proper_shapes = assert_proper_shapes

with ops.name_scope(name, values=[multiplier, num_rows]):
    self._multiplier = linear_operator_util.convert_nonref_to_tensor(
        multiplier, name="multiplier")

    # Check and auto-set hints.
    if not self._multiplier.dtype.is_complex:
        if is_self_adjoint is False:  # pylint: disable=g-bool-id-comparison
            raise ValueError("A real diagonal operator is always self adjoint.")
        else:
            is_self_adjoint = True

    if not is_square:
        raise ValueError("A ScaledIdentity operator is always square.")

    linear_operator_util.assert_not_ref_type(num_rows, "num_rows")

    super(LinearOperatorScaledIdentity, self).__init__(
        dtype=self._multiplier.dtype.base_dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)

    self._num_rows = linear_operator_util.shape_tensor(
        num_rows, name="num_rows")
    self._num_rows_static = tensor_util.constant_value(self._num_rows)
    self._check_num_rows_possibly_add_asserts()
    self._num_rows_cast_to_dtype = math_ops.cast(self._num_rows, self.dtype)
    self._num_rows_cast_to_real_dtype = math_ops.cast(self._num_rows,
                                                      self.dtype.real_dtype)
