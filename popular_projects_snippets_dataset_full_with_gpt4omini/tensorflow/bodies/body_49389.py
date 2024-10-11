# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates statistics for computing the element-wise mean.

    Args:
      values: Per-example value.
      sample_weight: Optional weighting of each example. Defaults to 1.

    Returns:
      Update op.
    """
values = math_ops.cast(values, self._dtype)
if not self._built:
    self._build(values.shape)
elif values.shape != self._shape:
    raise ValueError('MeanTensor input values must always have the same '
                     'shape. Expected shape (set during the first call): {}. '
                     'Got: {}'.format(self._shape, values.shape))

num_values = array_ops.ones_like(values)
if sample_weight is not None:
    sample_weight = math_ops.cast(sample_weight, self._dtype)

    # Update dimensions of weights to match with values if possible.
    values, _, sample_weight = losses_utils.squeeze_or_expand_dimensions(
        values, sample_weight=sample_weight)
    try:
        # Broadcast weights if possible.
        sample_weight = weights_broadcast_ops.broadcast_weights(
            sample_weight, values)
    except ValueError:
        # Reduce values to same ndim as weight array
        ndim = backend.ndim(values)
        weight_ndim = backend.ndim(sample_weight)
        values = math_ops.reduce_mean(
            values, axis=list(range(weight_ndim, ndim)))

    num_values = math_ops.multiply(num_values, sample_weight)
    values = math_ops.multiply(values, sample_weight)

update_total_op = self._total.assign_add(values)
with ops.control_dependencies([update_total_op]):
    exit(self._count.assign_add(num_values))
