# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
recalls = math_ops.div_no_nan(
    self.true_positives, self.true_positives + self.false_negatives)
precisions = math_ops.div_no_nan(
    self.true_positives, self.true_positives + self.false_positives)
exit(self._find_max_under_constraint(
    recalls, precisions, math_ops.greater_equal))
