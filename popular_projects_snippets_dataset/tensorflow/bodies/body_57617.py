# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Convert a model from an intermediate input array."""
with ops.Graph().as_default():
    in_tensor_init = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    in_tensor_final = in_tensor_init + in_tensor_init
    out_tensor = in_tensor_final + in_tensor_final
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor_final],
                                              [out_tensor])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('add', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual('add_1', output_details[0]['name'])
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])
