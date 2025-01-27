# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Sequential tf.keras model with default inputs."""
with test_context():
    self._getSequentialModel(include_custom_layer=True)

    converter = lite.TFLiteConverter.from_keras_model_file(
        self._keras_file, custom_objects=self._custom_objects)
    tflite_model = converter.convert()
    self.assertIsNotNone(tflite_model)

# Check tensor details of converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Check inference of converted model.
input_data = np.array([[1, 2, 3]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
tflite_result = interpreter.get_tensor(output_details[0]['index'])

keras_model = keras.models.load_model(
    self._keras_file, custom_objects=self._custom_objects)
keras_result = keras_model.predict(input_data)

np.testing.assert_almost_equal(tflite_result, keras_result, 5)
