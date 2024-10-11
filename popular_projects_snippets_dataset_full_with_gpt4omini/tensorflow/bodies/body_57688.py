# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Sequential tf.keras model with default inputs."""
with test_context():
    self._getSequentialModel()

    converter = lite.TFLiteConverter.from_keras_model_file(self._keras_file)
    tflite_model = converter.convert()
    self.assertIsNotNone(tflite_model)

# Check tensor details of converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEndsWith(input_details[0]['name'], 'dense_input')
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1, 3, 3], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])

# Check inference of converted model.
input_data = np.array([[1, 2, 3]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
tflite_result = interpreter.get_tensor(output_details[0]['index'])

keras_model = keras.models.load_model(self._keras_file)
keras_result = keras_model.predict(input_data)

np.testing.assert_almost_equal(tflite_result, keras_result, 5)
