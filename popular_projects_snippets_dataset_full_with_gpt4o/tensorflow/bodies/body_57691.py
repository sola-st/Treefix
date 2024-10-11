# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Sequential tf.keras model testing input shapes argument."""
self._getSequentialModel()

# Passing in shape of invalid input array raises error.
with self.assertRaises(ValueError) as error:
    converter = lite.TFLiteConverter.from_keras_model_file(
        self._keras_file, input_shapes={'invalid-input': [2, 3]})
self.assertEqual(
    "Invalid tensor 'invalid-input' found in tensor shapes map.",
    str(error.exception))

# Passing in shape of valid input array.
converter = lite.TFLiteConverter.from_keras_model_file(
    self._keras_file, input_shapes={'dense_input': [2, 3]})
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check input shape from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEndsWith(input_details[0]['name'], 'dense_input')
self.assertAllEqual([2, 3], input_details[0]['shape'])
