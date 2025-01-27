# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

def create_v1_saved_model():
    saved_model_dir = os.path.join(self.get_temp_dir(), 'resources_with_cond')
    with tf.Graph().as_default():
        with tf.compat.v1.Session() as sess:
            in_tensor = tf.compat.v1.placeholder(
                shape=[1], dtype=tf.float32, name='input')

            def body(i, arr):
                n = tf.raw_ops.StackPushV2(
                    handle=arr, elem=tf.cast(i, dtype=tf.float32))
                exit((n, arr))

            arr = tf.raw_ops.StackV2(max_size=10, elem_type=tf.float32)
            n, result_arr = tf.cond(in_tensor < 10, lambda: body(0, arr),
                                    lambda: body(1, arr))

            with ops.control_dependencies([result_arr, n]):
                out_tensor = tf.raw_ops.StackPopV2(
                    handle=result_arr, elem_type=tf.float32)

            inputs = {'x': in_tensor}
            outputs = {'a': out_tensor}
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
self.assertEqual(0.0, actual_value)
