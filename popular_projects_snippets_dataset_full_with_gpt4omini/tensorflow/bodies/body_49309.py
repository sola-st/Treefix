# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(MeanRelativeError, self).__init__(name=name, dtype=dtype)
normalizer = math_ops.cast(normalizer, self._dtype)
self.normalizer = normalizer
