# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
frozen_graph_def = self._constructGraphDef()

# Check metrics when conversion successed.
converter = lite.TFLiteConverter(frozen_graph_def, None, None,
                                 [('in_tensor', [2, 16, 16, 3])], ['add'])
mock_metrics = mock.create_autospec(
    metrics.TFLiteConverterMetrics, instance=True)
converter._tflite_metrics = mock_metrics
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
mock_metrics.assert_has_calls([
    mock.call.increase_counter_converter_attempt(),
    mock.call.increase_counter_converter_success(),
    mock.call.export_metrics(),
    mock.call.set_converter_param('input_format', '1'),
    mock.call.set_converter_param('enable_mlir_converter', 'True'),
    mock.call.set_converter_param('allow_custom_ops', 'False'),
    mock.call.set_converter_param('api_version', '1'),
], any_order=True)  # pyformat: disable
