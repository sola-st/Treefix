# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if specificity < 0 or specificity > 1:
    raise ValueError('`specificity` must be in the range [0, 1].')
self.specificity = specificity
self.num_thresholds = num_thresholds
super(SensitivityAtSpecificity, self).__init__(
    specificity,
    num_thresholds=num_thresholds,
    class_id=class_id,
    name=name,
    dtype=dtype)
