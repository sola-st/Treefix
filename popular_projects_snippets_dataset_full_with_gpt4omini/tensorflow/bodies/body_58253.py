# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable.py
super(TFLiteConverterMetrics, self).__init__()
session_id = uuid.uuid4().hex
self._metrics_exporter = metrics_wrapper.MetricsWrapper(session_id)
self._exported = False
