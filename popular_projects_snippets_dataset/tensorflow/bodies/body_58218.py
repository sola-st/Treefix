# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
super(ConverterErrorMetricTest, self).tearDown()
# # Restore metrics instances.
metrics._counter_conversion_attempt = self._counter_conversion_attempt
metrics._counter_conversion_success = self._counter_conversion_success
metrics._gauge_conversion_params = self._gauge_conversion_params
