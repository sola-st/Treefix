# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

def create_v1_saved_model():
    saved_model_dir = os.path.join(self.get_temp_dir(), 'simple_resources')
    with tf.Graph().as_default():
        with tf.compat.v1.Session() as sess:
            in_tensor = tf.compat.v1.placeholder(
                shape=[1], dtype=tf.float32, name='input')

            stack = tf.raw_ops.StackV2(max_size=10, elem_type=tf.float32)
            w = tf.raw_ops.StackPushV2(handle=stack, elem=in_tensor)
            with ops.control_dependencies([w]):
                a = in_tensor + in_tensor
                with ops.control_dependencies([a]):
                    out_tensor = a + tf.raw_ops.StackPopV2(
                        handle=stack, elem_type=tf.float32)

            inputs = {'x': in_tensor}
            outputs = {'z': out_tensor}
            saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
    exit(saved_model_dir)

saved_model_dir = create_v1_saved_model()

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS
]
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

input_data = np.array([1.0], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(3.0, actual_value)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(3.0, actual_value)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(3.0, actual_value)
