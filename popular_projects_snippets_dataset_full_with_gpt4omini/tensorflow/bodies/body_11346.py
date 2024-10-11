# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
r"""Initialize a `LinearOperatorIdentity`.

    The `LinearOperatorIdentity` is initialized with arguments defining `dtype`
    and shape.

    This operator is able to broadcast the leading (batch) dimensions, which
    sometimes requires copying data.  If `batch_shape` is `None`, the operator
    can take arguments of any batch shape without copying.  See examples.

    Args:
      num_rows:  Scalar non-negative integer `Tensor`.  Number of rows in the
        corresponding identity matrix.
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
      ValueError:  If `batch_shape` is determined statically to not be 1-D, or
        negative.
      ValueError:  If any of the following is not `True`:
        `{is_self_adjoint, is_non_singular, is_positive_definite}`.
      TypeError:  If `num_rows` or `batch_shape` is ref-type (e.g. Variable).
    """
parameters = dict(
    num_rows=num_rows,
    batch_shape=batch_shape,
    dtype=dtype,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    assert_proper_shapes=assert_proper_shapes,
    name=name)

dtype = dtype or dtypes.float32
self._assert_proper_shapes = assert_proper_shapes

with ops.name_scope(name):
    dtype = dtypes.as_dtype(dtype)
    if not is_self_adjoint:
        raise ValueError("An identity operator is always self adjoint.")
    if not is_non_singular:
        raise ValueError("An identity operator is always non-singular.")
    if not is_positive_definite:
        raise ValueError("An identity operator is always positive-definite.")
    if not is_square:
        raise ValueError("An identity operator is always square.")

    super(LinearOperatorIdentity, self).__init__(
        dtype=dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)

    linear_operator_util.assert_not_ref_type(num_rows, "num_rows")
    linear_operator_util.assert_not_ref_type(batch_shape, "batch_shape")

    self._num_rows = linear_operator_util.shape_tensor(
        num_rows, name="num_rows")
    self._num_rows_static = tensor_util.constant_value(self._num_rows)
    self._check_num_rows_possibly_add_asserts()

    if batch_shape is None:
        self._batch_shape_arg = None
    else:
        self._batch_shape_arg = linear_operator_util.shape_tensor(
            batch_shape, name="batch_shape_arg")
        self._batch_shape_static = tensor_util.constant_value(
            self._batch_shape_arg)
        self._check_batch_shape_possibly_add_asserts()
