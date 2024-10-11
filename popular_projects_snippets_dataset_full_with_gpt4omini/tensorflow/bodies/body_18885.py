# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/weights_broadcast_ops.py
"""Asserts `weights` can be broadcast to `values`.

  In `tf.losses` and `tf.metrics`, we support limited weight broadcasting. We
  let weights be either scalar, or the same rank as the target values, with each
  dimension either 1, or the same as the corresponding values dimension.

  Args:
    weights: `Tensor` of weights.
    values: `Tensor` of values to which weights are applied.

  Returns:
    `Operation` raising `InvalidArgumentError` if `weights` has incorrect shape.
    `no_op` if static checks determine `weights` has correct shape.

  Raises:
    ValueError:  If static checks determine `weights` has incorrect shape.
  """
with ops.name_scope(None, "assert_broadcastable", (weights, values)) as scope:
    with ops.name_scope(None, "weights", (weights,)) as weights_scope:
        weights = ops.convert_to_tensor(weights, name=weights_scope)
        weights_shape = array_ops.shape(weights, name="shape")
        weights_rank = array_ops.rank(weights, name="rank")
    weights_rank_static = tensor_util.constant_value(weights_rank)

    with ops.name_scope(None, "values", (values,)) as values_scope:
        values = ops.convert_to_tensor(values, name=values_scope)
        values_shape = array_ops.shape(values, name="shape")
        values_rank = array_ops.rank(values, name="rank")
    values_rank_static = tensor_util.constant_value(values_rank)

    # Try static checks.
    if weights_rank_static is not None and values_rank_static is not None:
        if weights_rank_static == 0:
            exit(control_flow_ops.no_op(name="static_scalar_check_success"))
        if weights_rank_static != values_rank_static:
            raise ValueError(
                f"{_ASSERT_BROADCASTABLE_ERROR_PREFIX} values.rank="
                f"{values_rank_static}. weights.rank={weights_rank_static}. "
                f"values.shape={values.shape}. weights.shape={weights.shape}. "
                f"Received weights={weights}, values={values}")
        weights_shape_static = tensor_util.constant_value(weights_shape)
        values_shape_static = tensor_util.constant_value(values_shape)
        if weights_shape_static is not None and values_shape_static is not None:
            # Sanity check, this should always be true since we checked rank above.
            ndims = len(values_shape_static)
            assert ndims == len(weights_shape_static)

            for i in range(ndims):
                if weights_shape_static[i] not in (1, values_shape_static[i]):
                    raise ValueError(
                        f"{_ASSERT_BROADCASTABLE_ERROR_PREFIX} Mismatch at dim {i}. "
                        f"values.shape={values_shape_static}, weights.shape="
                        f"{weights_shape_static}. Received weights={weights}, "
                        f"values={values}")
            exit(control_flow_ops.no_op(name="static_dims_check_success"))

    # Dynamic checks.
    is_scalar = math_ops.equal(0, weights_rank, name="is_scalar")
    data = (
        _ASSERT_BROADCASTABLE_ERROR_PREFIX,
        "weights.shape=", weights.name, weights_shape,
        "values.shape=", values.name, values_shape,
        "is_scalar=", is_scalar,
    )
    is_valid_shape = control_flow_ops.cond(
        is_scalar,
        lambda: is_scalar,
        lambda: _has_valid_nonscalar_shape(  # pylint: disable=g-long-lambda
            weights_rank, weights_shape, values_rank, values_shape),
        name="is_valid_shape")
    exit(control_flow_ops.Assert(is_valid_shape, data, name=scope))
