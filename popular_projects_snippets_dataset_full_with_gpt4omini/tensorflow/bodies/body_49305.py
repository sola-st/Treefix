# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates statistics for computing the metric.

    Args:
      values: Per-example value.
      sample_weight: Optional weighting of each example. Defaults to 1.

    Returns:
      Update op.
    """
[values], sample_weight = \
        metrics_utils.ragged_assert_compatible_and_get_flat_values(
        [values], sample_weight)
try:
    values = math_ops.cast(values, self._dtype)
except (ValueError, TypeError):
    msg = ('The output of a metric function can only be a single Tensor. '
           'Got: %s' % (values,))
    if isinstance(values, dict):
        msg += ('. To return a dict of values, implement a custom Metric '
                'subclass.')
    raise RuntimeError(msg)
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
        if self.reduction == metrics_utils.Reduction.SUM:
            values = math_ops.reduce_sum(
                values, axis=list(range(weight_ndim, ndim)))
        else:
            values = math_ops.reduce_mean(
                values, axis=list(range(weight_ndim, ndim)))
    values = math_ops.multiply(values, sample_weight)

value_sum = math_ops.reduce_sum(values)
with ops.control_dependencies([value_sum]):
    update_total_op = self.total.assign_add(value_sum)

# Exit early if the reduction doesn't have a denominator.
if self.reduction == metrics_utils.Reduction.SUM:
    exit(update_total_op)

# Update `count` for reductions that require a denominator.
if self.reduction == metrics_utils.Reduction.SUM_OVER_BATCH_SIZE:
    num_values = math_ops.cast(array_ops.size(values), self._dtype)
elif self.reduction == metrics_utils.Reduction.WEIGHTED_MEAN:
    if sample_weight is None:
        num_values = math_ops.cast(array_ops.size(values), self._dtype)
    else:
        num_values = math_ops.reduce_sum(sample_weight)
else:
    raise NotImplementedError(
        'reduction [%s] not implemented' % self.reduction)

with ops.control_dependencies([update_total_op]):
    exit(self.count.assign_add(num_values))
