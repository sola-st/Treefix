# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py

class ConvModel(autotrackable.AutoTrackable):

    @def_function.function
    def conv_func(self, in_tensor, filter_tensor):
        bias = constant_op.constant(3., shape=[1])
        conv_tensor = tf.nn.conv2d(
            in_tensor,
            filter_tensor,
            strides=[1, 1, 1, 1],
            dilations=[1, 1, 1, 1],
            padding='VALID',
            data_format='NHWC')
        conv_tensor = conv_tensor + bias
        exit(tf.nn.relu(conv_tensor))

root = ConvModel()
input_data = tf.reshape(tf.range(4, dtype=tf.float32), [1, 2, 2, 1])
filter_data = tf.reshape(tf.range(2, dtype=tf.float32), [1, 2, 1, 1])
concrete_func = root.conv_func.get_concrete_function(
    input_data, filter_data)

converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter._experimental_tf_quantization_mode = tf_quantization_mode
tflite_model = converter.convert()
self.assertTrue(tflite_model)
self.assertCountEqual(['CONV_2D', 'RESHAPE'],
                      tflite_test_util.get_ops_list(tflite_model))

# Check the model works.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
test_input = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32).reshape(
    (1, 2, 2, 1))
interpreter.set_tensor(input_details[0]['index'], test_input)
test_filter = np.array([1.0, 0.0], dtype=np.float32).reshape((1, 2, 1, 1))
interpreter.set_tensor(input_details[1]['index'], test_filter)
interpreter.invoke()

output_details = interpreter.get_output_details()
expected_output = np.array([[[[4.]], [[6.]]]], dtype=np.float32)
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertTrue((expected_output == output_data).all())
