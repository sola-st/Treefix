# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
saved_model_dir = self._createV1SavedModel(shape=[1, 16, 16, 3])
converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
tflite_metrics = converter._tflite_metrics
mock_exporter = mock.MagicMock()
tflite_metrics._metrics_exporter = mock_exporter
self.disable_converter_counter_metrics(tflite_metrics)
mock_exporter.ExportMetrics.assert_not_called()
tflite_metrics.__del__()
mock_exporter.ExportMetrics.assert_called_once()
