# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
# Construct a graph using a scalar (empty shape) input.
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(dtype=dtypes.float32, shape=[])
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Test conversion with the scalar input shape.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('Placeholder', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertEmpty(input_details[0]['shape'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual('add', output_details[0]['name'])
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertEmpty(input_details[0]['shape'])

# Validate inference using the scalar inputs/outputs.
test_input = np.array(4.0, dtype=np.float32)
expected_output = np.array(8.0, dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(expected_output, output_data)
