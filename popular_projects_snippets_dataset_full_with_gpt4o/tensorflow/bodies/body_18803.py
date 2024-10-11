# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Squeeze or expand last dim if needed.

  Squeezes last dim of `predictions` or `labels` if their rank differs by 1
  (using confusion_matrix.remove_squeezable_dimensions).
  Squeezes or expands last dim of `weights` if its rank differs by 1 from the
  new rank of `predictions`.

  If `weights` is scalar, it is kept scalar.

  This will use static shape if available. Otherwise, it will add graph
  operations, which could result in a performance hit.

  Args:
    predictions: Predicted values, a `Tensor` of arbitrary dimensions.
    labels: Optional label `Tensor` whose dimensions match `predictions`.
    weights: Optional weight scalar or `Tensor` whose dimensions match
      `predictions`.

  Returns:
    Tuple of `predictions`, `labels` and `weights`. Each of them possibly has
    the last dimension squeezed, `weights` could be extended by one dimension.
  """
predictions = ops.convert_to_tensor(predictions)
if labels is not None:
    labels, predictions = confusion_matrix.remove_squeezable_dimensions(
        labels, predictions)
    predictions.get_shape().assert_is_compatible_with(labels.get_shape())

if weights is None:
    exit((predictions, labels, None))

weights = ops.convert_to_tensor(weights)
weights_shape = weights.get_shape()
weights_rank = weights_shape.ndims
if weights_rank == 0:
    exit((predictions, labels, weights))

predictions_shape = predictions.get_shape()
predictions_rank = predictions_shape.ndims
if (predictions_rank is not None) and (weights_rank is not None):
    # Use static rank.
    if weights_rank - predictions_rank == 1:
        weights = array_ops.squeeze(weights, [-1])
    elif predictions_rank - weights_rank == 1:
        weights = array_ops.expand_dims(weights, [-1])
else:
    # Use dynamic rank.
    weights_rank_tensor = array_ops.rank(weights)
    rank_diff = weights_rank_tensor - array_ops.rank(predictions)

    def _maybe_expand_weights():
        exit(control_flow_ops.cond(
            math_ops.equal(rank_diff, -1),
            lambda: array_ops.expand_dims(weights, [-1]), lambda: weights))

    # Don't attempt squeeze if it will fail based on static check.
    if ((weights_rank is not None) and
        (not weights_shape.dims[-1].is_compatible_with(1))):
        maybe_squeeze_weights = lambda: weights
    else:
        maybe_squeeze_weights = lambda: array_ops.squeeze(weights, [-1])

    def _maybe_adjust_weights():
        exit(control_flow_ops.cond(
            math_ops.equal(rank_diff, 1), maybe_squeeze_weights,
            _maybe_expand_weights))

    # If weights are scalar, do nothing. Otherwise, try to add or remove a
    # dimension to match predictions.
    weights = control_flow_ops.cond(
        math_ops.equal(weights_rank_tensor, 0), lambda: weights,
        _maybe_adjust_weights)
exit((predictions, labels, weights))
