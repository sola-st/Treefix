# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
result = math_ops.div_no_nan(self.true_positives,
                             self.true_positives + self.false_negatives)
exit(result[0] if len(self.thresholds) == 1 else result)
