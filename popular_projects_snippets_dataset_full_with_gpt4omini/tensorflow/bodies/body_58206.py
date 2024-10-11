# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
model, func, calibration_gen = self._getIntegerQuantizeModel()

quantized_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                     model)
mock_metrics = mock.create_autospec(
    metrics.TFLiteConverterMetrics, instance=True)
quantized_converter._tflite_metrics = mock_metrics
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)
mock_metrics.assert_has_calls([
    mock.call.increase_counter_converter_attempt(),
    mock.call.increase_counter_converter_success(),
    mock.call.set_converter_param(
        'optimization_post_training_integer_quantize', 'True'),
    mock.call.set_converter_param('inference_type', 'tf.int8'),
    mock.call.set_converter_param('select_user_tf_ops', 'None'),
    mock.call.set_converter_param('activations_type', 'tf.int8'),
], any_order=True)  # pyformat: disable
