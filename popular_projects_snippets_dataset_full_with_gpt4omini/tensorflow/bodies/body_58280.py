# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
root = autotrackable.AutoTrackable()
root.add_func = def_function.function(lambda x: x + x)
input_data = tf.reshape(tf.range(4, dtype=tf.float32), [1, 4])
concrete_func = root.add_func.get_concrete_function(input_data)

# Convert model and check if the op is not flex.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter._experimental_tf_quantization_mode = tf_quantization_mode
tflite_model = converter.convert()
self.assertTrue(tflite_model)
if tf_quantization_mode == 'LEGACY_INTEGER':
    self.assertIn('ADD', tflite_test_util.get_ops_list(tflite_model))
else:
    self.assertIn('FlexAddV2', tflite_test_util.get_ops_list(tflite_model))

# Check the model works.
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
