# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Calculate per-step mean Intersection-Over-Union (mIOU).

  Mean Intersection-Over-Union is a common evaluation metric for
  semantic image segmentation, which first computes the IOU for each
  semantic class and then computes the average over classes.
  IOU is defined as follows:
    IOU = true_positive / (true_positive + false_positive + false_negative).
  The predictions are accumulated in a confusion matrix, weighted by `weights`,
  and mIOU is then calculated from it.

  For estimation of the metric over a stream of data, the function creates an
  `update_op` operation that updates these variables and returns the `mean_iou`.

  If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

  Args:
    labels: A `Tensor` of ground truth labels with shape [batch size] and of
      type `int32` or `int64`. The tensor will be flattened if its rank > 1.
    predictions: A `Tensor` of prediction results for semantic labels, whose
      shape is [batch size] and type `int32` or `int64`. The tensor will be
      flattened if its rank > 1.
    num_classes: The possible number of labels the prediction task can
      have. This value must be provided, since a confusion matrix of
      dimension = [num_classes, num_classes] will be allocated.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
      `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
      be either `1`, or the same as the corresponding `labels` dimension).
    metrics_collections: An optional list of collections that `mean_iou`
      should be added to.
    updates_collections: An optional list of collections `update_op` should be
      added to.
    name: An optional variable_scope name.

  Returns:
    mean_iou: A `Tensor` representing the mean intersection-over-union.
    update_op: An operation that increments the confusion matrix.

  Raises:
    ValueError: If `predictions` and `labels` have mismatched shapes, or if
      `weights` is not `None` and its shape doesn't match `predictions`, or if
      either `metrics_collections` or `updates_collections` are not a list or
      tuple.
    RuntimeError: If eager execution is enabled.
  """
if context.executing_eagerly():
    raise RuntimeError('tf.metrics.mean_iou is not supported when '
                       'eager execution is enabled.')

with variable_scope.variable_scope(name, 'mean_iou',
                                   (predictions, labels, weights)):
    # Check if shape is compatible.
    predictions.get_shape().assert_is_compatible_with(labels.get_shape())

    total_cm, update_op = _streaming_confusion_matrix(labels, predictions,
                                                      num_classes, weights)

    def compute_mean_iou(_, total_cm):
        """Compute the mean intersection-over-union via the confusion matrix."""
        sum_over_row = math_ops.cast(
            math_ops.reduce_sum(total_cm, 0), dtypes.float32)
        sum_over_col = math_ops.cast(
            math_ops.reduce_sum(total_cm, 1), dtypes.float32)
        cm_diag = math_ops.cast(array_ops.diag_part(total_cm), dtypes.float32)
        denominator = sum_over_row + sum_over_col - cm_diag

        # The mean is only computed over classes that appear in the
        # label or prediction tensor. If the denominator is 0, we need to
        # ignore the class.
        num_valid_entries = math_ops.reduce_sum(
            math_ops.cast(
                math_ops.not_equal(denominator, 0), dtype=dtypes.float32))

        # If the value of the denominator is 0, set it to 1 to avoid
        # zero division.
        denominator = array_ops.where(
            math_ops.greater(denominator, 0), denominator,
            array_ops.ones_like(denominator))
        iou = math_ops.divide(cm_diag, denominator)

        # If the number of valid entries is 0 (no classes) we return 0.
        result = array_ops.where(
            math_ops.greater(num_valid_entries, 0),
            math_ops.reduce_sum(iou, name='mean_iou') / num_valid_entries, 0)
        exit(result)

    # TODO(priyag): Use outside_compilation if in TPU context.
    mean_iou_v = _aggregate_across_replicas(
        metrics_collections, compute_mean_iou, total_cm)

    if updates_collections:
        ops.add_to_collections(updates_collections, update_op)

    exit((mean_iou_v, update_op))
