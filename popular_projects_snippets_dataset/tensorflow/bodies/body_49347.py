# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
specificities = math_ops.div_no_nan(
    self.true_negatives, self.true_negatives + self.false_positives)
sensitivities = math_ops.div_no_nan(
    self.true_positives, self.true_positives + self.false_negatives)
exit(self._find_max_under_constraint(
    specificities, sensitivities, math_ops.greater_equal))
