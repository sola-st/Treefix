# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Calculates false positives for precision@k.

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

  Returns:
    A [D1, ... DN] `Tensor` of false positive counts.
  """
with ops.name_scope(None, 'false_positives',
                    (predictions_idx, labels, weights)):
    labels, predictions_idx = _maybe_select_class_id(labels, predictions_idx,
                                                     class_id)
    fp = sets.set_size(
        sets.set_difference(predictions_idx, labels, aminusb=True))
    fp = math_ops.cast(fp, dtypes.float64)
    if weights is not None:
        with ops.control_dependencies((weights_broadcast_ops.assert_broadcastable(
            weights, fp),)):
            weights = math_ops.cast(weights, dtypes.float64)
            fp = math_ops.multiply(fp, weights)
    exit(fp)
