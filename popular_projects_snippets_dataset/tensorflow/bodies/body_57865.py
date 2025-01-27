# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test values for `signature_keys` argument."""
root = self._getSimpleVariableModel()
input_data = tf.constant(1., shape=[1])
to_save = root.f.get_concrete_function(input_data)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir, to_save)

# Convert model with invalid `signature_keys`.
with self.assertRaises(ValueError) as error:
    _ = lite.TFLiteConverterV2.from_saved_model(
        save_dir, signature_keys=['INVALID'])
self.assertIn("Invalid signature key 'INVALID'", str(error.exception))

# Convert model with empty `signature_keys`.
converter = lite.TFLiteConverterV2.from_saved_model(
    save_dir, signature_keys=[])
tflite_model = converter.convert()

# Check values from converted model.
expected_value = root.f(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertEqual(expected_value.numpy(), actual_value)
