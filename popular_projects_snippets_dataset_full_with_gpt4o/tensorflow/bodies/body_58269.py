# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(shape=[1, 4], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
converter.target_ops = set([lite.OpsSet.SELECT_TF_OPS])

# Ensure `target_ops` is set to the correct value after flag deprecation.
self.assertEqual(converter.target_ops, set([lite.OpsSet.SELECT_TF_OPS]))
self.assertEqual(converter.target_spec.supported_ops,
                 set([lite.OpsSet.SELECT_TF_OPS]))

tflite_model = converter.convert()
self.assertTrue(tflite_model)

# Check the model works with TensorFlow ops.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
test_input = np.array([[1.0, 2.0, 3.0, 4.0]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_details = interpreter.get_output_details()
expected_output = np.array([[2.0, 4.0, 6.0, 8.0]], dtype=np.float32)
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
