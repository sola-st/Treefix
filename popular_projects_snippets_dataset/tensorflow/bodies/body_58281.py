# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
root = autotrackable.AutoTrackable()
root.l2_loss_func = def_function.function(lambda x: nn_ops.l2_loss(x))  # pylint: disable=unnecessary-lambda
input_data = tf.range(4, dtype=tf.float32)
concrete_func = root.l2_loss_func.get_concrete_function(input_data)

converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter._experimental_tf_quantization_mode = tf_quantization_mode
tflite_model = converter.convert()
self.assertTrue(tflite_model)
self.assertIn('FlexL2Loss', tflite_test_util.get_ops_list(tflite_model))

# Check the model works.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
test_input = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_details = interpreter.get_output_details()
expected_output = np.array([15.0], dtype=np.float32)
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
