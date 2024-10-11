# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root = self._getSimpleVariableModel()
input_data = tf.constant(1., shape=[1])
concrete_func = root.f.get_concrete_function(input_data)

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.SELECT_TF_OPS
]
tflite_model = converter.convert()
# Check the conversion metadata.
metadata = get_conversion_metadata(tflite_model)
self.assertIsNotNone(metadata)
self.assertEqual(metadata.options.forceSelectTfOps, True)

# Check output value from converted model.
expected_value = root.f(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertEqual(expected_value.numpy(), actual_value)
