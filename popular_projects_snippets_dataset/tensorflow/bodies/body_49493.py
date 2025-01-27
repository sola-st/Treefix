# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
"""Squeeze last dim if ranks differ from expected by exactly 1.

  In the common case where we expect shapes to match, `expected_rank_diff`
  defaults to 0, and we squeeze the last dimension of the larger rank if they
  differ by 1.

  But, for example, if `labels` contains class IDs and `predictions` contains 1
  probability per class, we expect `predictions` to have 1 more dimension than
  `labels`, so `expected_rank_diff` would be 1. In this case, we'd squeeze
  `labels` if `rank(predictions) - rank(labels) == 0`, and
  `predictions` if `rank(predictions) - rank(labels) == 2`.

  This will use static shape if available. Otherwise, it will add graph
  operations, which could result in a performance hit.

  Args:
    labels: Label values, a `Tensor` whose dimensions match `predictions`.
    predictions: Predicted values, a `Tensor` of arbitrary dimensions.
    expected_rank_diff: Expected result of `rank(predictions) - rank(labels)`.
    name: Name of the op.

  Returns:
    Tuple of `labels` and `predictions`, possibly with last dim squeezed.
  """
with backend.name_scope(name or 'remove_squeezable_dimensions'):
    if not isinstance(predictions, ragged_tensor.RaggedTensor):
        predictions = ops.convert_to_tensor_v2_with_dispatch(predictions)
    if not isinstance(labels, ragged_tensor.RaggedTensor):
        labels = ops.convert_to_tensor_v2_with_dispatch(labels)
    predictions_shape = predictions.shape
    predictions_rank = predictions_shape.ndims
    labels_shape = labels.shape
    labels_rank = labels_shape.ndims
    if (labels_rank is not None) and (predictions_rank is not None):
        # Use static rank.
        rank_diff = predictions_rank - labels_rank
        if (rank_diff == expected_rank_diff + 1 and
            predictions_shape.dims[-1].is_compatible_with(1)):
            predictions = array_ops.squeeze(predictions, [-1])
        elif (rank_diff == expected_rank_diff - 1 and
              labels_shape.dims[-1].is_compatible_with(1)):
            labels = array_ops.squeeze(labels, [-1])
        exit((labels, predictions))

    # Use dynamic rank.
    rank_diff = array_ops.rank(predictions) - array_ops.rank(labels)
    if (predictions_rank is None) or (
        predictions_shape.dims[-1].is_compatible_with(1)):
        predictions = control_flow_ops.cond(
            math_ops.equal(expected_rank_diff + 1, rank_diff),
            lambda: array_ops.squeeze(predictions, [-1]),
            lambda: predictions)
    if (labels_rank is None) or (
        labels_shape.dims[-1].is_compatible_with(1)):
        labels = control_flow_ops.cond(
            math_ops.equal(expected_rank_diff - 1, rank_diff),
            lambda: array_ops.squeeze(labels, [-1]),
            lambda: labels)
    exit((labels, predictions))
