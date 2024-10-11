# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Interpolation formula inspired by section 4 of Davis & Goadrich 2006.

    https://www.biostat.wisc.edu/~page/rocpr.pdf

    Note here we derive & use a closed formula not present in the paper
    as follows:

      Precision = TP / (TP + FP) = TP / P

    Modeling all of TP (true positive), FP (false positive) and their sum
    P = TP + FP (predicted positive) as varying linearly within each interval
    [A, B] between successive thresholds, we get

      Precision slope = dTP / dP
                      = (TP_B - TP_A) / (P_B - P_A)
                      = (TP - TP_A) / (P - P_A)
      Precision = (TP_A + slope * (P - P_A)) / P

    The area within the interval is (slope / total_pos_weight) times

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

    Returns:
      pr_auc: an approximation of the area under the P-R curve.
    """
dtp = self.true_positives[:self.num_thresholds -
                          1] - self.true_positives[1:]
p = self.true_positives + self.false_positives
dp = p[:self.num_thresholds - 1] - p[1:]
prec_slope = math_ops.div_no_nan(
    dtp, math_ops.maximum(dp, 0), name='prec_slope')
intercept = self.true_positives[1:] - math_ops.multiply(prec_slope, p[1:])

safe_p_ratio = array_ops.where(
    math_ops.logical_and(p[:self.num_thresholds - 1] > 0, p[1:] > 0),
    math_ops.div_no_nan(
        p[:self.num_thresholds - 1],
        math_ops.maximum(p[1:], 0),
        name='recall_relative_ratio'),
    array_ops.ones_like(p[1:]))

pr_auc_increment = math_ops.div_no_nan(
    prec_slope * (dtp + intercept * math_ops.log(safe_p_ratio)),
    math_ops.maximum(self.true_positives[1:] + self.false_negatives[1:], 0),
    name='pr_auc_increment')

if self.multi_label:
    by_label_auc = math_ops.reduce_sum(
        pr_auc_increment, name=self.name + '_by_label', axis=0)
    if self.label_weights is None:
        # Evenly weighted average of the label AUCs.
        exit(math_ops.reduce_mean(by_label_auc, name=self.name))
    else:
        # Weighted average of the label AUCs.
        exit(math_ops.div_no_nan(
            math_ops.reduce_sum(
                math_ops.multiply(by_label_auc, self.label_weights)),
            math_ops.reduce_sum(self.label_weights),
            name=self.name))
else:
    exit(math_ops.reduce_sum(pr_auc_increment, name='interpolate_pr_auc'))
