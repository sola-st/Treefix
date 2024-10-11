# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a SavedModel with the input_shapes arugment."""
saved_model_dir = self._createSavedModel(shape=[None, 16, 16, 3])

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_saved_model(
    saved_model_dir,
    input_shapes={
        'inputA': [2, 16, 16, 3],
        'inputB': [2, 16, 16, 3]
    })
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertStartsWith(input_details[0]['name'], 'inputA')
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([2, 16, 16, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

self.assertStartsWith(input_details[1]['name'], 'inputB')
self.assertEqual(np.float32, input_details[1]['dtype'])
self.assertAllEqual([2, 16, 16, 3], input_details[1]['shape'])
self.assertEqual((0., 0.), input_details[1]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertStartsWith(output_details[0]['name'], 'add')
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([2, 16, 16, 3], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])
