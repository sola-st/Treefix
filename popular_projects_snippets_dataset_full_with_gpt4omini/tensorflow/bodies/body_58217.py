# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
super(ConverterErrorMetricTest, self).setUp()

# Mock metrics instance except errors so other test cases are not affected.
mock_attempt = mock.create_autospec(monitoring.Counter, instance=True)
self._counter_conversion_attempt = metrics._counter_conversion_attempt
metrics._counter_conversion_attempt = mock_attempt

mock_success = mock.create_autospec(monitoring.Counter, instance=True)
self._counter_conversion_success = metrics._counter_conversion_success
metrics._counter_conversion_success = mock_success

mock_params = mock.create_autospec(monitoring.StringGauge, instance=True)
self._gauge_conversion_params = metrics._gauge_conversion_params
metrics._gauge_conversion_params = mock_params
