# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

def create_v1_saved_model():
    saved_model_dir = os.path.join(self.get_temp_dir(), 'variants_with_cond')
    with tf.Graph().as_default():
        with tf.compat.v1.Session() as sess:
            m = map_ops.empty_tensor_map()

            def body(i, m):
                m = map_ops.tensor_map_insert(m, i, i)
                exit((i + 1, m))

            in_tensor = tf.compat.v1.placeholder(
                shape=[1], dtype=tf.int32, name='input')
            _, result_m = tf.cond(in_tensor < 10, lambda: body(in_tensor, m),
                                  lambda: body(in_tensor + 1, m))
            out_tensor = in_tensor + map_ops.tensor_map_size(result_m)

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

input_data = np.array([0], dtype=np.int32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
expected_value = np.array([1], dtype=np.int32)
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(expected_value, actual_value)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(expected_value, actual_value)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(expected_value, actual_value)
