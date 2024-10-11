# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if precision < 0 or precision > 1:
    raise ValueError('`precision` must be in the range [0, 1].')
self.precision = precision
self.num_thresholds = num_thresholds
super(RecallAtPrecision, self).__init__(
    value=precision,
    num_thresholds=num_thresholds,
    class_id=class_id,
    name=name,
    dtype=dtype)
