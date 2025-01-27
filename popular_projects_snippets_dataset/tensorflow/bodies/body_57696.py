# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Functional tf.keras model with input shape overriding."""
self._getFunctionalModelMultipleInputs()

# Convert to TFLite model.
converter = lite.TFLiteConverter.from_keras_model_file(
    self._keras_file, input_shapes={
        'input_a': {2, 3},
        'input_b': {2, 3}
    })
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertEndsWith(input_details[0]['name'], 'input_a')
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([2, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

self.assertEndsWith(input_details[1]['name'], 'input_b')
self.assertEqual(np.float32, input_details[1]['dtype'])
self.assertAllEqual([2, 3], input_details[1]['shape'])
self.assertEqual((0., 0.), input_details[1]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 2)
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([2, 4], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])

self.assertEqual(np.float32, output_details[1]['dtype'])
self.assertAllEqual([2, 4], output_details[1]['shape'])
self.assertEqual((0., 0.), output_details[1]['quantization'])
