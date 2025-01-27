# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
op_resolver_types = [
    interpreter_wrapper.OpResolverType.BUILTIN,
    interpreter_wrapper.OpResolverType.BUILTIN_REF,
    interpreter_wrapper.OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES
]

for op_resolver_type in op_resolver_types:
    interpreter = interpreter_wrapper.Interpreter(
        model_path=resource_loader.get_path_to_datafile(
            'testdata/permute_float.tflite'),
        experimental_op_resolver_type=op_resolver_type)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    self.assertEqual(1, len(input_details))
    self.assertEqual('input', input_details[0]['name'])
    self.assertEqual(np.float32, input_details[0]['dtype'])
    self.assertTrue(([1, 4] == input_details[0]['shape']).all())
    self.assertEqual((0.0, 0), input_details[0]['quantization'])
    self.assertQuantizationParamsEqual(
        [], [], 0, input_details[0]['quantization_parameters'])

    output_details = interpreter.get_output_details()
    self.assertEqual(1, len(output_details))
    self.assertEqual('output', output_details[0]['name'])
    self.assertEqual(np.float32, output_details[0]['dtype'])
    self.assertTrue(([1, 4] == output_details[0]['shape']).all())
    self.assertEqual((0.0, 0), output_details[0]['quantization'])
    self.assertQuantizationParamsEqual(
        [], [], 0, output_details[0]['quantization_parameters'])

    test_input = np.array([[1.0, 2.0, 3.0, 4.0]], dtype=np.float32)
    expected_output = np.array([[4.0, 3.0, 2.0, 1.0]], dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], test_input)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    self.assertTrue((expected_output == output_data).all())
