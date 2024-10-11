# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

@tf.function(input_signature=[tf.TensorSpec(shape=[1], dtype=tf.float32)])
def model(v):
    m = map_ops.empty_tensor_map()
    k = tf.constant(1.0)
    p = tf.add(k, v)
    with ops.control_dependencies([m]):
        m2 = map_ops.tensor_map_insert(m, p, v)
        with ops.control_dependencies([m2]):
            exit(map_ops.tensor_map_size(m2))

concrete_func = model.get_concrete_function()

converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
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
self.assertEqual(1, actual_value)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(1, actual_value)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(1, actual_value)
