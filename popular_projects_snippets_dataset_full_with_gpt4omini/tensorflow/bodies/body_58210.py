# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
saved_model_dir = self._createV1SavedModel(shape=[1, 16, 16, 3])

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.experimental_new_converter = False
mock_metrics = mock.create_autospec(
    metrics.TFLiteConverterMetrics, instance=True)
converter._tflite_metrics = mock_metrics
converter.convert()
mock_metrics.assert_has_calls([
    mock.call.increase_counter_converter_attempt(),
    mock.call.increase_counter_converter_success(),
    mock.call.export_metrics(),
    mock.call.set_converter_param('enable_mlir_converter', 'False'),
    mock.call.set_converter_param('api_version', '2'),
], any_order=True)  # pyformat: disable
