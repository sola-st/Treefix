# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a calibration with custom op registered by function."""
saved_model_dir, calibration_gen = self._createGraphWithCustomOp()

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.optimizations = [lite.Optimize.DEFAULT]
converter.representative_dataset = calibration_gen
converter.allow_custom_ops = True
converter.target_spec._experimental_custom_op_registerers = [
    test_registerer.TF_TestRegisterer
]
tflite_model = converter.convert()
self.assertTrue(tflite_model)
self.assertGreater(test_registerer.get_num_test_registerer_calls(), 0)
self.assertIn('Double', tflite_test_util.get_ops_list(tflite_model))

# Check the model works with custom ops.
interpreter = InterpreterWithCustomOps(
    model_content=tflite_model,
    custom_op_registerers=[test_registerer.TF_TestRegisterer])
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
test_input = np.array([[0.0, 0.1, 0.2, 0.3]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

output_details = interpreter.get_output_details()
expected_output = np.array([[0.0, 0.2, 0.4, 0.6]], dtype=np.float32)
output_data = interpreter.get_tensor(output_details[0]['index'])
self.assertArrayNear(expected_output[0], output_data[0], err=1e-2)
