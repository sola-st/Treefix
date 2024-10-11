# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(shape=[4], dtype=dtypes.string)
    out_tensor = array_ops.reshape(in_tensor, shape=[2, 2])
    sess = session.Session()

# Convert model and ensure model is not None.
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
self.assertEqual(np.string_, input_details[0]['dtype'])
self.assertAllEqual([4], input_details[0]['shape'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual('Reshape', output_details[0]['name'])
self.assertEqual(np.string_, output_details[0]['dtype'])
self.assertAllEqual([2, 2], output_details[0]['shape'])
