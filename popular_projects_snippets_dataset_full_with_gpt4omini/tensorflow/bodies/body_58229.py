# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
input_tensor1 = tf.keras.layers.Input(
    shape=[None, None, 2, 3, 3], dtype=tf.complex64)
input_tensor2 = tf.keras.layers.Input(
    shape=[None, None, 2, 3, 3], dtype=tf.complex64)
output = tf.keras.layers.Add()([input_tensor1, input_tensor2])
model = tf.keras.Model(
    inputs=[input_tensor1, input_tensor2], outputs=output)
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.experimental_lower_to_saved_model = lower_to_saved_model
# The location does not contain callsite to the current file.
self.convert_and_check_location_info(
    converter,
    converter_error_data_pb2.ConverterErrorData.CALLSITELOC,
    expected_sources=[expected_source] if expected_source else None)
