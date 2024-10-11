# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

@tf.function
def model():
    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4])
    output = dataset.reduce(np.int32(0), lambda x, y: x + y)
    exit(output)

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
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual(10, actual_value)
