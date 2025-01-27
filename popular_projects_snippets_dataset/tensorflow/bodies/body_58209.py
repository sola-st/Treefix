# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
saved_model_dir = self._createV1SavedModel(shape=[1, 16, 16, 3])
converter = lite.TFLiteSavedModelConverter(saved_model_dir, set(['serve']),
                                           ['serving_default'])
converter.experimental_new_converter = True
mock_metrics = mock.create_autospec(
    metrics.TFLiteConverterMetrics, instance=True)
converter._tflite_metrics = mock_metrics
time.process_time = mock.Mock(side_effect=np.arange(1, 1000, 2).tolist())
converter.convert()
mock_metrics.assert_has_calls([
    mock.call.increase_counter_converter_attempt(),
    mock.call.increase_counter_converter_success(),
    mock.call.set_converter_latency(2000),
    mock.call.export_metrics(),
    mock.call.set_converter_param('enable_mlir_converter', 'True'),
], any_order=True)  # pyformat: disable
