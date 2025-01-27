# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

def create_v1_saved_model():
    saved_model_dir = os.path.join(self.get_temp_dir(),
                                   'simple_mutable_variable')
    with tf.Graph().as_default():
        with tf.compat.v1.Session() as sess:
            in_tensor = tf.compat.v1.placeholder(
                shape=[1], dtype=tf.float32, name='input')

            ta = tf.TensorArray(
                tf.float32, size=3, dynamic_size=False, clear_after_read=False)
            ta = ta.write(0, 10.0)
            ta = ta.write(1, 20.0)
            ta = ta.write(2, 30.0)

            out_tensor = ta.read(0) + ta.read(2)

            inputs = {'x': in_tensor}
            outputs = {'z': out_tensor}
            saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
    exit(saved_model_dir)

saved_model_dir = create_v1_saved_model()

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
if not lower_tensor_list_ops:
    converter.target_spec.supported_ops = [
        tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS
    ]
converter._experimental_lower_tensor_list_ops = lower_tensor_list_ops
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
self.assertEqual(40.0, actual_value)
