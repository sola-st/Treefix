# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]
model = tf.keras.models.Sequential(
    [tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=1)
converter = lite.TFLiteConverterV2.from_keras_model(model)
mock_metrics = mock.create_autospec(
    metrics.TFLiteConverterMetrics, instance=True)
converter._tflite_metrics = mock_metrics
converter.convert()
mock_metrics.assert_has_calls([
    mock.call.increase_counter_converter_attempt(),
    mock.call.increase_counter_converter_success(),
    mock.call.export_metrics(),
    mock.call.set_converter_param('inference_type', 'tf.float32'),
    mock.call.set_converter_param('target_ops', 'TFLITE_BUILTINS'),
    mock.call.set_converter_param('optimization_default', 'False'),
], any_order=True)  # pyformat: disable
