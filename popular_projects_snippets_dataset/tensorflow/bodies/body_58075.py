# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/permute_float.tflite'),
    num_threads=2)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
test_input = np.array([[1.0, 2.0, 3.0, 4.0]], dtype=np.float32)
expected_output = np.array([[4.0, 3.0, 2.0, 1.0]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_details = interpreter.get_output_details()
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
