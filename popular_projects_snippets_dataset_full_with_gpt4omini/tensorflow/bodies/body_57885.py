# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a SavedModel with an unknown input shape."""
saved_model_dir = self._createModelWithInputShape(None)

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
self.assertTrue(tflite_model)

# Validate that tensors with unknown shape have unknown rank.
tflite_model_obj = _convert_bytearray_to_object(tflite_model)
for tensor in tflite_model_obj.subgraphs[0].tensors:
    self.assertEqual(False, tensor.hasRank)
    self.assertEqual([], tensor.shape.tolist())

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_data = np.array([1., 2., 3.], dtype=np.float32)
interpreter.resize_tensor_input(
    input_details[0]['index'], [3], strict=False)
interpreter.allocate_tensors()

interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertEqual([2., 4., 6.], list(actual_value))
