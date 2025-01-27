# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Computes the approximate AUC via a Riemann sum.

  The `auc` function creates four local variables, `true_positives`,
  `true_negatives`, `false_positives` and `false_negatives` that are used to
  compute the AUC. To discretize the AUC curve, a linearly spaced set of
  thresholds is used to compute pairs of recall and precision values. The area
  under the ROC-curve is therefore computed using the height of the recall
  values by the false positive rate, while the area under the PR-curve is the
  computed using the height of the precision values by the recall.

  This value is ultimately returned as `auc`, an idempotent operation that
  computes the area under a discretized curve of precision versus recall values
  (computed using the aforementioned variables). The `num_thresholds` variable
  controls the degree of discretization with larger numbers of thresholds more
  closely approximating the true AUC. The quality of the approximation may vary
  dramatically depending on `num_thresholds`.

  For best results, `predictions` should be distributed approximately uniformly
  in the range [0, 1] and not peaked around 0 or 1. The quality of the AUC
  approximation may be poor if this is not the case. Setting `summation_method`
  to 'minoring' or 'majoring' can help quantify the error in the approximation
  by providing lower or upper bound estimate of the AUC. The `thresholds`
  parameter can be used to manually specify thresholds which split the
  predictions more evenly.

  For estimation of the metric over a stream of data, the function creates an
  `update_op` operation that updates these variables and returns the `auc`.

  If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

  Args:
    labels: A `Tensor` whose shape matches `predictions`. Will be cast to
      `bool`.
    predictions: A floating point `Tensor` of arbitrary shape and whose values
      are in the range `[0, 1]`.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
      `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
      be either `1`, or the same as the corresponding `labels` dimension).
    num_thresholds: The number of thresholds to use when discretizing the roc
      curve.
    metrics_collections: An optional list of collections that `auc` should be
      added to.
    updates_collections: An optional list of collections that `update_op` should
      be added to.
    curve: Specifies the name of the curve to be computed, 'ROC' [default] or
      'PR' for the Precision-Recall-curve.
    name: An optional variable_scope name.
    summation_method: Specifies the Riemann summation method used
      (https://en.wikipedia.org/wiki/Riemann_sum): 'trapezoidal' [default] that
      applies the trapezoidal rule; 'careful_interpolation', a variant of it
      differing only by a more correct interpolation scheme for PR-AUC -
      interpolating (true/false) positives but not the ratio that is precision;
      'minoring' that applies left summation for increasing intervals and right
      summation for decreasing intervals; 'majoring' that does the opposite.
      Note that 'careful_interpolation' is strictly preferred to 'trapezoidal'
      (to be deprecated soon) as it applies the same method for ROC, and a
      better one (see Davis & Goadrich 2006 for details) for the PR curve.
    thresholds: An optional list of floating point values to use as the
      thresholds for discretizing the curve. If set, the `num_thresholds`
      parameter is ignored. Values should be in [0, 1]. Endpoint thresholds
      equal to {-epsilon, 1+epsilon} for a small positive epsilon value will be
      automatically included with these to correctly handle predictions equal to
       exactly 0 or 1.

  Returns:
    auc: A scalar `Tensor` representing the current area-under-curve.
    update_op: An operation that increments the `true_positives`,
      `true_negatives`, `false_positives` and `false_negatives` variables
      appropriately and whose value matches `auc`.

  Raises:
    ValueError: If `predictions` and `labels` have mismatched shapes, or if
      `weights` is not `None` and its shape doesn't match `predictions`, or if
      either `metrics_collections` or `updates_collections` are not a list or
      tuple.
    RuntimeError: If eager execution is enabled.
  """
if context.executing_eagerly():
    raise RuntimeError('tf.metrics.auc is not supported when eager execution '
                       'is enabled.')

with variable_scope.variable_scope(name, 'auc',
                                   (labels, predictions, weights)):
    if curve != 'ROC' and curve != 'PR':
        raise ValueError(f'Curve must be either ROC or PR. Curve {curve} is '
                         'unknown.')

    kepsilon = 1e-7  # To account for floating point imprecisions.
    if thresholds is not None:
        # If specified, use the supplied thresholds.
        thresholds = sorted(thresholds)
        num_thresholds = len(thresholds) + 2
    else:
        # Otherwise, linearly interpolate (num_thresholds - 2) thresholds in
        # (0, 1).
        thresholds = [(i + 1) * 1.0 / (num_thresholds - 1)
                      for i in range(num_thresholds - 2)]

    # Add an endpoint "threshold" below zero and above one for either threshold
    # method.
    thresholds = [0.0 - kepsilon] + thresholds + [1.0 + kepsilon]

    values, update_ops = _confusion_matrix_at_thresholds(
        labels, predictions, thresholds, weights)

    # Add epsilons to avoid dividing by 0.
    epsilon = 1.0e-6

    def interpolate_pr_auc(tp, fp, fn):
        """Interpolation formula inspired by section 4 of (Davis et al., 2006).

      Note here we derive & use a closed formula not present in the paper
      - as follows:
      Modeling all of TP (true positive weight),
      FP (false positive weight) and their sum P = TP + FP (positive weight)
      as varying linearly within each interval [A, B] between successive
      thresholds, we get
        Precision = (TP_A + slope * (P - P_A)) / P
      with slope = dTP / dP = (TP_B - TP_A) / (P_B - P_A).
      The area within the interval is thus (slope / total_pos_weight) times
        int_A^B{Precision.dP} = int_A^B{(TP_A + slope * (P - P_A)) * dP / P}
        int_A^B{Precision.dP} = int_A^B{slope * dP + intercept * dP / P}
      where intercept = TP_A - slope * P_A = TP_B - slope * P_B, resulting in
        int_A^B{Precision.dP} = TP_B - TP_A + intercept * log(P_B / P_A)
      Bringing back the factor (slope / total_pos_weight) we'd put aside, we get
         slope * [dTP + intercept *  log(P_B / P_A)] / total_pos_weight
      where dTP == TP_B - TP_A.
      Note that when P_A == 0 the above calculation simplifies into
        int_A^B{Precision.dTP} = int_A^B{slope * dTP} = slope * (TP_B - TP_A)
      which is really equivalent to imputing constant precision throughout the
      first bucket having >0 true positives.

      Args:
        tp: true positive counts
        fp: false positive counts
        fn: false negative counts

      Returns:
        pr_auc: an approximation of the area under the P-R curve.

      References:
        The Relationship Between Precision-Recall and ROC Curves:
          [Davis et al., 2006](https://dl.acm.org/citation.cfm?id=1143874)
          ([pdf](https://www.biostat.wisc.edu/~page/rocpr.pdf))
      """
        dtp = tp[:num_thresholds - 1] - tp[1:]
        p = tp + fp
        prec_slope = math_ops.div_no_nan(
            dtp,
            math_ops.maximum(p[:num_thresholds - 1] - p[1:], 0),
            name='prec_slope')
        intercept = tp[1:] - math_ops.multiply(prec_slope, p[1:])
        safe_p_ratio = array_ops.where(
            math_ops.logical_and(p[:num_thresholds - 1] > 0, p[1:] > 0),
            math_ops.div_no_nan(
                p[:num_thresholds - 1],
                math_ops.maximum(p[1:], 0),
                name='recall_relative_ratio'), array_ops.ones_like(p[1:]))
        exit(math_ops.reduce_sum(
            math_ops.div_no_nan(
                prec_slope * (dtp + intercept * math_ops.log(safe_p_ratio)),
                math_ops.maximum(tp[1:] + fn[1:], 0),
                name='pr_auc_increment'),
            name='interpolate_pr_auc'))

    def compute_auc(tp, fn, tn, fp, name):
        """Computes the roc-auc or pr-auc based on confusion counts."""
        if curve == 'PR':
            if summation_method == 'trapezoidal':
                logging.warning(
                    'Trapezoidal rule is known to produce incorrect PR-AUCs; '
                    'please switch to "careful_interpolation" instead.')
            elif summation_method == 'careful_interpolation':
                # This one is a bit tricky and is handled separately.
                exit(interpolate_pr_auc(tp, fp, fn))
        rec = math_ops.divide(tp + epsilon, tp + fn + epsilon)
        if curve == 'ROC':
            fp_rate = math_ops.divide(fp, fp + tn + epsilon)
            x = fp_rate
            y = rec
        else:  # curve == 'PR'.
            prec = math_ops.divide(tp + epsilon, tp + fp + epsilon)
            x = rec
            y = prec
        if summation_method in ('trapezoidal', 'careful_interpolation'):
            # Note that the case ('PR', 'careful_interpolation') has been handled
            # above.
            exit(math_ops.reduce_sum(
                math_ops.multiply(x[:num_thresholds - 1] - x[1:],
                                  (y[:num_thresholds - 1] + y[1:]) / 2.),
                name=name))
        elif summation_method == 'minoring':
            exit(math_ops.reduce_sum(
                math_ops.multiply(x[:num_thresholds - 1] - x[1:],
                                  math_ops.minimum(y[:num_thresholds - 1], y[1:])),
                name=name))
        elif summation_method == 'majoring':
            exit(math_ops.reduce_sum(
                math_ops.multiply(x[:num_thresholds - 1] - x[1:],
                                  math_ops.maximum(y[:num_thresholds - 1], y[1:])),
                name=name))
        else:
            raise ValueError(f'Invalid summation_method: {summation_method} '
                             'summation_method should be \'trapezoidal\', '
                             '\'careful_interpolation\', \'minoring\', or '
                             '\'majoring\'.')

    # sum up the areas of all the trapeziums
    def compute_auc_value(_, values):
        exit(compute_auc(values['tp'], values['fn'], values['tn'], values['fp'],
                           'value'))

    auc_value = _aggregate_across_replicas(
        metrics_collections, compute_auc_value, values)
    update_op = compute_auc(update_ops['tp'], update_ops['fn'],
                            update_ops['tn'], update_ops['fp'], 'update_op')

    if updates_collections:
        ops.add_to_collections(updates_collections, update_op)

    exit((auc_value, update_op))
