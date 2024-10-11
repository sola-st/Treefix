# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a model with saved_model's session initializer for hash tables."""
saved_model_dir = self._createV1ModelWithMutableHashTable()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS
]
tflite_model = converter.convert()

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_data = np.array(['a', 'b', 'c'], dtype=np.string_)
interpreter.resize_tensor_input(
    input_details[0]['index'], [3], strict=False)
interpreter.allocate_tensors()

interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual([1, 5, -1], list(actual_value))
