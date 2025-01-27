# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
model_path = resource_loader.get_path_to_datafile(
    'testdata/permute_uint8.tflite')
with io.open(model_path, 'rb') as model_file:
    data = model_file.read()

interpreter = interpreter_wrapper.Interpreter(model_content=data)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertEqual(1, len(input_details))
self.assertEqual('input', input_details[0]['name'])
self.assertEqual(np.uint8, input_details[0]['dtype'])
self.assertTrue(([1, 4] == input_details[0]['shape']).all())
self.assertEqual((1.0, 0), input_details[0]['quantization'])
self.assertQuantizationParamsEqual(
    [1.0], [0], 0, input_details[0]['quantization_parameters'])

output_details = interpreter.get_output_details()
self.assertEqual(1, len(output_details))
self.assertEqual('output', output_details[0]['name'])
self.assertEqual(np.uint8, output_details[0]['dtype'])
self.assertTrue(([1, 4] == output_details[0]['shape']).all())
self.assertEqual((1.0, 0), output_details[0]['quantization'])
self.assertQuantizationParamsEqual(
    [1.0], [0], 0, output_details[0]['quantization_parameters'])

test_input = np.array([[1, 2, 3, 4]], dtype=np.uint8)
expected_output = np.array([[4, 3, 2, 1]], dtype=np.uint8)
interpreter.resize_tensor_input(input_details[0]['index'], test_input.shape)
interpreter.allocate_tensors()
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
