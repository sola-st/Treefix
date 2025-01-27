# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
precisions = math_ops.div_no_nan(
    self.true_positives, self.true_positives + self.false_positives)
recalls = math_ops.div_no_nan(
    self.true_positives, self.true_positives + self.false_negatives)
exit(self._find_max_under_constraint(
    precisions, recalls, math_ops.greater_equal))
