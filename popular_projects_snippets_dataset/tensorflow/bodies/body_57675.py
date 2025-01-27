# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a SavedModel, with None in input tensor's shape."""
saved_model_dir = self._createSavedModel(shape=[None, 16, 16, 3])

converter = lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertStartsWith(input_details[0]['name'], 'inputA')
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

self.assertStartsWith(input_details[1]['name'], 'inputB')
self.assertEqual(np.float32, input_details[1]['dtype'])
self.assertAllEqual([1, 16, 16, 3], input_details[1]['shape'])
self.assertEqual((0., 0.), input_details[1]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertStartsWith(output_details[0]['name'], 'add')
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])
