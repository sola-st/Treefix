# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if self._built:
    confusion_matrix_variables = (self.true_positives, self.true_negatives,
                                  self.false_positives, self.false_negatives)
    if self.multi_label:
        backend.batch_set_value(
            [(v, np.zeros((self.num_thresholds, self._num_labels)))
             for v in confusion_matrix_variables])
    else:
        backend.batch_set_value([(v, np.zeros((self.num_thresholds,)))
                                 for v in confusion_matrix_variables])
