# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
num_thresholds = len(to_list(self.thresholds))
backend.batch_set_value([(v, np.zeros((num_thresholds,)))
                         for v in (self.true_positives,
                                   self.false_positives)])
