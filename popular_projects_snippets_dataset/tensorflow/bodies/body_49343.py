# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
num_thresholds = len(self.thresholds)
confusion_matrix_variables = (self.true_positives, self.true_negatives,
                              self.false_positives, self.false_negatives)
backend.batch_set_value([
    (v, np.zeros((num_thresholds,))) for v in confusion_matrix_variables
])
