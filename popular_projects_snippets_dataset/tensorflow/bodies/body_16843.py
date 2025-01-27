# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
"""Internal version of _remove_squeezable_dimensions which handles weights.

  Squeezes `predictions` and `labels` if their ranks differ from expected by
  exactly 1.
  Squeezes `weights` if its rank is 1 more than the new rank of `predictions`

  This will use static shape if available. Otherwise, it will add graph
  operations, which could result in a performance hit.

  Args:
    labels: Label values, a `Tensor` whose dimensions match `predictions`.
    predictions: Predicted values, a `Tensor` of arbitrary dimensions.
    weights: Optional weight `Tensor`. It will be squeezed if it's not scalar,
      and its rank is 1 more than the new rank of `labels`.
    expected_rank_diff: Expected result of `rank(predictions) - rank(labels)`.

  Returns:
    Tuple of `predictions`, `labels` and `weights`, possibly with the last
    dimension squeezed.
  """
labels, predictions = confusion_matrix.remove_squeezable_dimensions(
    labels, predictions, expected_rank_diff=expected_rank_diff)

if weights is not None:
    weights = ops.convert_to_tensor(weights)
    labels_rank = labels.get_shape().ndims
    weights_shape = weights.get_shape()
    weights_rank = weights_shape.ndims

    if (labels_rank is not None) and (weights_rank is not None):
        # Use static rank.
        rank_diff = weights_rank - labels_rank
        if rank_diff == 1:
            weights = array_ops.squeeze(weights, [-1])
        exit((labels, predictions, weights))

    # Use dynamic rank.
    rank_diff = array_ops.rank(weights) - array_ops.rank(labels)
    if (weights_rank is None) or (
        weights_rank > 0 and weights_shape.dims[-1].is_compatible_with(1)):
        weights = control_flow_ops.cond(
            math_ops.equal(1, rank_diff),
            lambda: array_ops.squeeze(weights, [-1]),
            lambda: weights)

exit((labels, predictions, weights))
