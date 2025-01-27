# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Computes true_positives, false_negatives, true_negatives, false_positives.

  This function creates up to four local variables, `true_positives`,
  `true_negatives`, `false_positives` and `false_negatives`.
  `true_positive[i]` is defined as the total weight of values in `predictions`
  above `thresholds[i]` whose corresponding entry in `labels` is `True`.
  `false_negatives[i]` is defined as the total weight of values in `predictions`
  at most `thresholds[i]` whose corresponding entry in `labels` is `True`.
  `true_negatives[i]` is defined as the total weight of values in `predictions`
  at most `thresholds[i]` whose corresponding entry in `labels` is `False`.
  `false_positives[i]` is defined as the total weight of values in `predictions`
  above `thresholds[i]` whose corresponding entry in `labels` is `False`.

  For estimation of these metrics over a stream of data, for each metric the
  function respectively creates an `update_op` operation that updates the
  variable and returns its value.

  If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

  Args:
    labels: A `Tensor` whose shape matches `predictions`. Will be cast to
      `bool`.
    predictions: A floating point `Tensor` of arbitrary shape and whose values
      are in the range `[0, 1]`.
    thresholds: A python list or tuple of float thresholds in `[0, 1]`.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
      `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
      be either `1`, or the same as the corresponding `labels` dimension).
    includes: Tuple of keys to return, from 'tp', 'fn', 'tn', fp'. If `None`,
        default to all four.

  Returns:
    values: Dict of variables of shape `[len(thresholds)]`. Keys are from
        `includes`.
    update_ops: Dict of operations that increments the `values`. Keys are from
        `includes`.

  Raises:
    ValueError: If `predictions` and `labels` have mismatched shapes, or if
      `weights` is not `None` and its shape doesn't match `predictions`, or if
      `includes` contains invalid keys.
  """
all_includes = ('tp', 'fn', 'tn', 'fp')
if includes is None:
    includes = all_includes
else:
    for include in includes:
        if include not in all_includes:
            raise ValueError(f'Invalid key: {include}')

with ops.control_dependencies([
    check_ops.assert_greater_equal(
        predictions,
        math_ops.cast(0.0, dtype=predictions.dtype),
        message='predictions must be in [0, 1]'),
    check_ops.assert_less_equal(
        predictions,
        math_ops.cast(1.0, dtype=predictions.dtype),
        message='predictions must be in [0, 1]')
]):
    predictions, labels, weights = _remove_squeezable_dimensions(
        predictions=math_ops.cast(predictions, dtypes.float32),
        labels=math_ops.cast(labels, dtype=dtypes.bool),
        weights=weights)

num_thresholds = len(thresholds)

# Reshape predictions and labels.
predictions_2d = array_ops.reshape(predictions, [-1, 1])
labels_2d = array_ops.reshape(
    math_ops.cast(labels, dtype=dtypes.bool), [1, -1])

# Use static shape if known.
num_predictions = predictions_2d.get_shape().as_list()[0]

# Otherwise use dynamic shape.
if num_predictions is None:
    num_predictions = array_ops.shape(predictions_2d)[0]
thresh_tiled = array_ops.tile(
    array_ops.expand_dims(array_ops.constant(thresholds), [1]),
    array_ops.stack([1, num_predictions]))

# Tile the predictions after thresholding them across different thresholds.
pred_is_pos = math_ops.greater(
    array_ops.tile(array_ops.transpose(predictions_2d), [num_thresholds, 1]),
    thresh_tiled)
if ('fn' in includes) or ('tn' in includes):
    pred_is_neg = math_ops.logical_not(pred_is_pos)

# Tile labels by number of thresholds
label_is_pos = array_ops.tile(labels_2d, [num_thresholds, 1])
if ('fp' in includes) or ('tn' in includes):
    label_is_neg = math_ops.logical_not(label_is_pos)

if weights is not None:
    weights = weights_broadcast_ops.broadcast_weights(
        math_ops.cast(weights, dtypes.float32), predictions)
    weights_tiled = array_ops.tile(
        array_ops.reshape(weights, [1, -1]), [num_thresholds, 1])
    thresh_tiled.get_shape().assert_is_compatible_with(
        weights_tiled.get_shape())
else:
    weights_tiled = None

values = {}
update_ops = {}

if 'tp' in includes:
    true_p = metric_variable(
        [num_thresholds], dtypes.float32, name='true_positives')
    is_true_positive = math_ops.cast(
        math_ops.logical_and(label_is_pos, pred_is_pos), dtypes.float32)
    if weights_tiled is not None:
        is_true_positive *= weights_tiled
    update_ops['tp'] = state_ops.assign_add(true_p,
                                            math_ops.reduce_sum(
                                                is_true_positive, 1))
    values['tp'] = true_p

if 'fn' in includes:
    false_n = metric_variable(
        [num_thresholds], dtypes.float32, name='false_negatives')
    is_false_negative = math_ops.cast(
        math_ops.logical_and(label_is_pos, pred_is_neg), dtypes.float32)
    if weights_tiled is not None:
        is_false_negative *= weights_tiled
    update_ops['fn'] = state_ops.assign_add(false_n,
                                            math_ops.reduce_sum(
                                                is_false_negative, 1))
    values['fn'] = false_n

if 'tn' in includes:
    true_n = metric_variable(
        [num_thresholds], dtypes.float32, name='true_negatives')
    is_true_negative = math_ops.cast(
        math_ops.logical_and(label_is_neg, pred_is_neg), dtypes.float32)
    if weights_tiled is not None:
        is_true_negative *= weights_tiled
    update_ops['tn'] = state_ops.assign_add(true_n,
                                            math_ops.reduce_sum(
                                                is_true_negative, 1))
    values['tn'] = true_n

if 'fp' in includes:
    false_p = metric_variable(
        [num_thresholds], dtypes.float32, name='false_positives')
    is_false_positive = math_ops.cast(
        math_ops.logical_and(label_is_neg, pred_is_pos), dtypes.float32)
    if weights_tiled is not None:
        is_false_positive *= weights_tiled
    update_ops['fp'] = state_ops.assign_add(false_p,
                                            math_ops.reduce_sum(
                                                is_false_positive, 1))
    values['fp'] = false_p

exit((values, update_ops))
