# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/gather_string.tflite'))
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertEqual(2, len(input_details))
self.assertEqual('input', input_details[0]['name'])
self.assertEqual(np.string_, input_details[0]['dtype'])
self.assertTrue(([10] == input_details[0]['shape']).all())
self.assertEqual((0.0, 0), input_details[0]['quantization'])
self.assertQuantizationParamsEqual(
    [], [], 0, input_details[0]['quantization_parameters'])
self.assertEqual('indices', input_details[1]['name'])
self.assertEqual(np.int64, input_details[1]['dtype'])
self.assertTrue(([3] == input_details[1]['shape']).all())
self.assertEqual((0.0, 0), input_details[1]['quantization'])
self.assertQuantizationParamsEqual(
    [], [], 0, input_details[1]['quantization_parameters'])

output_details = interpreter.get_output_details()
self.assertEqual(1, len(output_details))
self.assertEqual('output', output_details[0]['name'])
self.assertEqual(np.string_, output_details[0]['dtype'])
self.assertTrue(([3] == output_details[0]['shape']).all())
self.assertEqual((0.0, 0), output_details[0]['quantization'])
self.assertQuantizationParamsEqual(
    [], [], 0, output_details[0]['quantization_parameters'])

test_input = np.array([1, 2, 3], dtype=np.int64)
interpreter.set_tensor(input_details[1]['index'], test_input)

test_input = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
expected_output = np.array([b'b', b'c', b'd'])
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
