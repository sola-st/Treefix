# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
stub = metrics.TFLiteMetrics()
stub.set_converter_param('name1', 'value1')
stub.set_converter_param('name2', 'value2')
self.assertEqual(
    metrics._gauge_conversion_params.get_cell('name1').value(), 'value1')
self.assertEqual(
    metrics._gauge_conversion_params.get_cell('name2').value(), 'value2')
