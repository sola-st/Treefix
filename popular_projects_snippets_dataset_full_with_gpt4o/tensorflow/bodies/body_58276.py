# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
# Create a graph that has one double op.
saved_model_dir = os.path.join(self.get_temp_dir(), 'model2')
with ops.Graph().as_default():
    with session.Session() as sess:
        in_tensor = array_ops.placeholder(
            shape=[1, 4], dtype=dtypes.int32, name='input')
        out_tensor = double_op.double(in_tensor)
        inputs = {'x': in_tensor}
        outputs = {'z': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = set([lite.OpsSet.SELECT_TF_OPS])
converter.target_spec.experimental_select_user_tf_ops = ['Double']
tflite_model = converter.convert()
self.assertTrue(tflite_model)
self.assertIn('FlexDouble', tflite_test_util.get_ops_list(tflite_model))

# Check the model works with TensorFlow ops.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
test_input = np.array([[1.0, 2.0, 3.0, 4.0]], dtype=np.int32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_details = interpreter.get_output_details()
expected_output = np.array([[2.0, 4.0, 6.0, 8.0]], dtype=np.int32)
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
