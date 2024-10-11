# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
data = b'abcd' + bytes(16)
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/gather_string_0d.tflite'))
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
interpreter.set_tensor(input_details[0]['index'], np.array(data))
test_input_tensor = interpreter.get_tensor(input_details[0]['index'])
self.assertEqual(len(data), len(test_input_tensor.item(0)))
