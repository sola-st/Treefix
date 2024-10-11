# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Calculates true positives for recall@k and precision@k.

  If `class_id` is specified, calculate binary true positives for `class_id`
      only.
  If `class_id` is not specified, calculate metrics for `k` predicted vs
      `n` label classes, where `n` is the 2nd dimension of `labels_sparse`.

  Args:
    labels: `int64` `Tensor` or `SparseTensor` with shape
      [D1, ... DN, num_labels], where N >= 1 and num_labels is the number of
      target classes for the associated prediction. Commonly, N=1 and `labels`
      has shape [batch_size, num_labels]. [D1, ... DN] must match
      `predictions_idx`.
    predictions_idx: 1-D or higher `int64` `Tensor` with last dimension `k`,
      top `k` predicted classes. For rank `n`, the first `n-1` dimensions must
      match `labels`.
    class_id: Class for which we want binary metrics.
    weights: `Tensor` whose rank is either 0, or n-1, where n is the rank of
      `labels`. If the latter, it must be broadcastable to `labels` (i.e., all
      dimensions must be either `1`, or the same as the corresponding `labels`
      dimension).
    name: Name of operation.

  Returns:
    A [D1, ... DN] `Tensor` of true positive counts.
  """
with ops.name_scope(name, 'true_positives',
                    (predictions_idx, labels, weights)):
    labels, predictions_idx = _maybe_select_class_id(labels, predictions_idx,
                                                     class_id)
    tp = sets.set_size(sets.set_intersection(predictions_idx, labels))
    tp = math_ops.cast(tp, dtypes.float64)
    if weights is not None:
        with ops.control_dependencies((weights_broadcast_ops.assert_broadcastable(
            weights, tp),)):
            weights = math_ops.cast(weights, dtypes.float64)
            tp = math_ops.multiply(tp, weights)
    exit(tp)
