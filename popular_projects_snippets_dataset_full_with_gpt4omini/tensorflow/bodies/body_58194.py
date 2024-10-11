# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
stub = metrics.TFLiteMetrics()
stub.increase_counter_converter_attempt()
self.assertEqual(metrics._counter_conversion_attempt.get_cell().value(), 1)
