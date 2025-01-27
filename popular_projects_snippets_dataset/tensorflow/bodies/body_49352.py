# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if recall < 0 or recall > 1:
    raise ValueError('`recall` must be in the range [0, 1].')
self.recall = recall
self.num_thresholds = num_thresholds
super(PrecisionAtRecall, self).__init__(
    value=recall,
    num_thresholds=num_thresholds,
    class_id=class_id,
    name=name,
    dtype=dtype)
