# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
frozen_graph_def = self._constructGraphDef()

# Check metrics when conversion failed.
converter = lite.TFLiteConverter(frozen_graph_def, None, None,
                                 [('wrong_tensor', [2, 16, 16, 3])],
                                 ['add'])
mock_metrics = mock.create_autospec(
    metrics.TFLiteConverterMetrics, instance=True)
converter._tflite_metrics = mock_metrics
with self.assertRaises(ConverterError):
    converter.convert()
mock_metrics.assert_has_calls([
    mock.call.increase_counter_converter_attempt(),
    mock.call.set_converter_param('output_format', '2'),
    mock.call.set_converter_param('select_user_tf_ops', 'None'),
    mock.call.set_converter_param('post_training_quantize', 'False'),
], any_order=True)  # pyformat: disable
mock_metrics.increase_counter_converter_success.assert_not_called()
