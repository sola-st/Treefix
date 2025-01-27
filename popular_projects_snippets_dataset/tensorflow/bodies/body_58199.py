# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
stub = metrics.TFLiteMetrics()
stub.set_converter_latency(34566)
self.assertEqual(metrics._gauge_conversion_latency.get_cell().value(),
                 34566)
