# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    var = variable_scope.get_variable(
        'weights', shape=[1, 16, 16, 3], dtype=dtypes.float32)
    # Get the second output to ensure freezing properly processes tensor names
    # like 'X:1'.
    out_tensor = nn_ops.top_k(in_tensor + var, name='top_k')[1]
    sess = session.Session()
    sess.run(_global_variables_initializer())

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
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual('top_k:1', output_details[0]['name'])
self.assertEqual(np.int32, output_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 1], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])
