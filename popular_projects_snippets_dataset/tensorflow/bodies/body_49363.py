# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if (self.curve == metrics_utils.AUCCurve.PR and
    self.summation_method == metrics_utils.AUCSummationMethod.INTERPOLATION
   ):
    # This use case is different and is handled separately.
    exit(self.interpolate_pr_auc())

# Set `x` and `y` values for the curves based on `curve` config.
recall = math_ops.div_no_nan(self.true_positives,
                             self.true_positives + self.false_negatives)
if self.curve == metrics_utils.AUCCurve.ROC:
    fp_rate = math_ops.div_no_nan(self.false_positives,
                                  self.false_positives + self.true_negatives)
    x = fp_rate
    y = recall
else:  # curve == 'PR'.
    precision = math_ops.div_no_nan(
        self.true_positives, self.true_positives + self.false_positives)
    x = recall
    y = precision

# Find the rectangle heights based on `summation_method`.
if self.summation_method == metrics_utils.AUCSummationMethod.INTERPOLATION:
    # Note: the case ('PR', 'interpolation') has been handled above.
    heights = (y[:self.num_thresholds - 1] + y[1:]) / 2.
elif self.summation_method == metrics_utils.AUCSummationMethod.MINORING:
    heights = math_ops.minimum(y[:self.num_thresholds - 1], y[1:])
else:  # self.summation_method = metrics_utils.AUCSummationMethod.MAJORING:
    heights = math_ops.maximum(y[:self.num_thresholds - 1], y[1:])

# Sum up the areas of all the rectangles.
if self.multi_label:
    riemann_terms = math_ops.multiply(x[:self.num_thresholds - 1] - x[1:],
                                      heights)
    by_label_auc = math_ops.reduce_sum(
        riemann_terms, name=self.name + '_by_label', axis=0)

    if self.label_weights is None:
        # Unweighted average of the label AUCs.
        exit(math_ops.reduce_mean(by_label_auc, name=self.name))
    else:
        # Weighted average of the label AUCs.
        exit(math_ops.div_no_nan(
            math_ops.reduce_sum(
                math_ops.multiply(by_label_auc, self.label_weights)),
            math_ops.reduce_sum(self.label_weights),
            name=self.name))
else:
    exit(math_ops.reduce_sum(
        math_ops.multiply(x[:self.num_thresholds - 1] - x[1:], heights),
        name=self.name))
