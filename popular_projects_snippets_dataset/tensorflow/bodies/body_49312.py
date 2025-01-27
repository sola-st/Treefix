# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(MeanMetricWrapper, self).__init__(name=name, dtype=dtype)
self._fn = fn
self._fn_kwargs = kwargs
