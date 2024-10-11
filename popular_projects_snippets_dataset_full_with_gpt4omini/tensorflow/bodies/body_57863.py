# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a basic model with Variables with saving/loading the SavedModel."""
root = self._getSimpleVariableModel()
input_data = tf.constant(1., shape=[1])
to_save = root.f.get_concrete_function(input_data)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir, to_save)

# Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_saved_model(save_dir)
tflite_model = converter.convert()
# Check the conversion metadata.
metadata = get_conversion_metadata(tflite_model)
self.assertIsNotNone(metadata)
self.assertEqual(metadata.environment.modelType,
                 metadata_fb.ModelType.TF_SAVED_MODEL)

# Check values from converted model.
expected_value = root.f(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertEqual(expected_value.numpy(), actual_value)
