# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
stub = metrics.TFLiteMetrics()
stub.set_converter_param('name', 'value')
self.assertEqual(
    metrics._gauge_conversion_params.get_cell('name').value(), 'value')
