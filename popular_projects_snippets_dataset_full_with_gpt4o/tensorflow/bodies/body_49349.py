# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if sensitivity < 0 or sensitivity > 1:
    raise ValueError('`sensitivity` must be in the range [0, 1].')
self.sensitivity = sensitivity
self.num_thresholds = num_thresholds
super(SpecificityAtSensitivity, self).__init__(
    sensitivity,
    num_thresholds=num_thresholds,
    class_id=class_id,
    name=name,
    dtype=dtype)
