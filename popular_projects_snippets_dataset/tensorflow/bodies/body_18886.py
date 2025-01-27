# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/weights_broadcast_ops.py
"""Broadcast `weights` to the same shape as `values`.

  This returns a version of `weights` following the same broadcast rules as
  `mul(weights, values)`, but limited to the weights shapes allowed by
  `assert_broadcastable`. When computing a weighted average, use this function
  to broadcast `weights` before summing them; e.g.,
  `reduce_sum(w * v) / reduce_sum(_broadcast_weights(w, v))`.

  Args:
    weights: `Tensor` whose shape is broadcastable to `values` according to the
      rules of `assert_broadcastable`.
    values: `Tensor` of any shape.

  Returns:
    `weights` broadcast to `values` shape according to the rules of
      `assert_broadcastable`.
  """
with ops.name_scope(None, "broadcast_weights", (weights, values)) as scope:
    values = ops.convert_to_tensor(values, name="values")
    weights = ops.convert_to_tensor(
        weights, dtype=values.dtype.base_dtype, name="weights")

    # Try static check for exact match.
    weights_shape = weights.get_shape()
    values_shape = values.get_shape()
    if (weights_shape.is_fully_defined() and
        values_shape.is_fully_defined() and
        weights_shape.is_compatible_with(values_shape)):
        exit(weights)

    # Skip the assert_broadcastable on TPU/GPU because asserts are not
    # supported so it only causes unnecessary ops. Also skip it because it uses
    # a DenseToDenseSetOperation op that is incompatible with the TPU/GPU when
    # the shape(s) are dynamic.
    if control_flow_ops.get_enclosing_xla_context() is not None:
        exit(math_ops.multiply(
            weights, array_ops.ones_like(values), name=scope))
    with ops.control_dependencies((assert_broadcastable(weights, values),)):
        exit(math_ops.multiply(
            weights, array_ops.ones_like(values), name=scope))
