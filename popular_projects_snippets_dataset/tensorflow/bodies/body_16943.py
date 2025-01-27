# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Returns the frequency-weighted mean and variance of `x`.

  Args:
    x: A tensor.
    axes: 1-d tensor of int32 values; these are the axes along which
      to compute mean and variance.
    frequency_weights: A tensor of positive weights which can be
      broadcast with x.
    name: Name used to scope the operation.
    keep_dims: Produce moments with the same dimensionality as the input.
    keepdims: Alias of keep_dims.

  Returns:
    Two tensors: `weighted_mean` and `weighted_variance`.
  """
keep_dims = deprecated_argument_lookup(
    "keepdims", keepdims, "keep_dims", keep_dims)
if keep_dims is None:
    keep_dims = False
with ops.name_scope(name, "weighted_moments", [x, frequency_weights, axes]):
    x = ops.convert_to_tensor(x, name="x")
    frequency_weights = ops.convert_to_tensor(
        frequency_weights, name="frequency_weights")

    # Unlike moments(), this just uses a simpler two-pass method.

    # See comment in moments() WRT precision; it applies here too.
    needs_cast = x.dtype == dtypes.float16
    if needs_cast:
        x = math_ops.cast(x, dtypes.float32)

    if frequency_weights.dtype != x.dtype:
        frequency_weights = math_ops.cast(frequency_weights, x.dtype)

    # Note that we use keep_dims=True for our reductions regardless of the arg;
    # this is so that the results remain broadcast-compatible with the inputs.
    weighted_input_sum = math_ops.reduce_sum(
        frequency_weights * x, axes, name="weighted_input_sum", keepdims=True)

    # The shape of the weights isn't necessarily the same as x's
    # shape, just broadcast-compatible with it -- so this expression
    # performs broadcasting to give a per-item weight, with the same
    # shape as (frequency_weights * x). This avoids having to reason
    # through all the broadcast logic to compute a correct
    # sum_of_weights.
    broadcasted_weights = frequency_weights + array_ops.zeros_like(x)

    sum_of_weights = math_ops.reduce_sum(
        broadcasted_weights, axes, name="sum_of_weights", keepdims=True)

    divisor = math_ops.reciprocal(sum_of_weights, name="inv_weight_sum")

    weighted_mean = math_ops.multiply(weighted_input_sum, divisor)

    # Have the weighted mean; now on to variance:
    weighted_distsq = math_ops.reduce_sum(
        frequency_weights * math_ops.squared_difference(x, weighted_mean),
        axes,
        name="weighted_distsq",
        keepdims=True)

    weighted_variance = math_ops.multiply(weighted_distsq, divisor)

    if not keep_dims:
        weighted_mean = array_ops.squeeze(weighted_mean, axis=axes)
        weighted_variance = array_ops.squeeze(
            weighted_variance, axis=axes)

    if needs_cast:
        weighted_mean = math_ops.cast(weighted_mean, dtypes.float16)
        weighted_variance = math_ops.cast(weighted_variance, dtypes.float16)

    exit((weighted_mean, weighted_variance))
