# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
r"""Initialize a `LinearOperatorZeros`.

    The `LinearOperatorZeros` is initialized with arguments defining `dtype`
    and shape.

    This operator is able to broadcast the leading (batch) dimensions, which
    sometimes requires copying data.  If `batch_shape` is `None`, the operator
    can take arguments of any batch shape without copying.  See examples.

    Args:
      num_rows:  Scalar non-negative integer `Tensor`.  Number of rows in the
        corresponding zero matrix.
      num_columns:  Scalar non-negative integer `Tensor`.  Number of columns in
        the corresponding zero matrix. If `None`, defaults to the value of
        `num_rows`.
      batch_shape:  Optional `1-D` integer `Tensor`.  The shape of the leading
        dimensions.  If `None`, this operator has no leading dimensions.
      dtype:  Data type of the matrix that this operator represents.
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
      ValueError:  If `num_columns` is determined statically to be non-scalar,
        or negative.
      ValueError:  If `batch_shape` is determined statically to not be 1-D, or
        negative.
      ValueError:  If any of the following is not `True`:
        `{is_self_adjoint, is_non_singular, is_positive_definite}`.
    """
parameters = dict(
    num_rows=num_rows,
    num_columns=num_columns,
    batch_shape=batch_shape,
    dtype=dtype,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    assert_proper_shapes=assert_proper_shapes,
    name=name
)

dtype = dtype or dtypes.float32
self._assert_proper_shapes = assert_proper_shapes

with ops.name_scope(name):
    dtype = dtypes.as_dtype(dtype)
    if not is_self_adjoint and is_square:
        raise ValueError("A zero operator is always self adjoint.")
    if is_non_singular:
        raise ValueError("A zero operator is always singular.")
    if is_positive_definite:
        raise ValueError("A zero operator is always not positive-definite.")

    super(LinearOperatorZeros, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)

    linear_operator_util.assert_not_ref_type(num_rows, "num_rows")
    linear_operator_util.assert_not_ref_type(num_columns, "num_columns")
    linear_operator_util.assert_not_ref_type(batch_shape, "batch_shape")

    self._num_rows = linear_operator_util.shape_tensor(
        num_rows, name="num_rows")
    self._num_rows_static = tensor_util.constant_value(self._num_rows)

    if num_columns is None:
        num_columns = num_rows

    self._num_columns = linear_operator_util.shape_tensor(
        num_columns, name="num_columns")
    self._num_columns_static = tensor_util.constant_value(self._num_columns)

    self._check_domain_range_possibly_add_asserts()

    if (self._num_rows_static is not None and
        self._num_columns_static is not None):
        if is_square and self._num_rows_static != self._num_columns_static:
            raise ValueError(
                "LinearOperatorZeros initialized as is_square=True, but got "
                "num_rows({}) != num_columns({})".format(
                    self._num_rows_static,
                    self._num_columns_static))

    if batch_shape is None:
        self._batch_shape_arg = None
    else:
        self._batch_shape_arg = linear_operator_util.shape_tensor(
            batch_shape, name="batch_shape_arg")
        self._batch_shape_static = tensor_util.constant_value(
            self._batch_shape_arg)
        self._check_batch_shape_possibly_add_asserts()
