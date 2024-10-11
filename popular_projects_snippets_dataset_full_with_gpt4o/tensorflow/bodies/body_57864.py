# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a basic model with Variables with saving/loading the SavedModel."""
root = self._getSimpleModelWithVariables()
input_data = tf.constant(1., shape=[1, 10])
to_save = root.assign_add.get_concrete_function(input_data)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir, to_save)

# Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_saved_model(save_dir)
converter.experimental_enable_resource_variables = enable_resource_variables

if not enable_resource_variables:
    with self.assertRaises(convert.ConverterError) as error:
        tflite_model = converter.convert()
    self.assertIn(
        'Variable constant folding is failed. Please consider using enabling '
        '`experimental_enable_resource_variables` flag in the TFLite '
        'converter object.',
        str(error.exception))
    exit()

# Enable resource variables.
tflite_model = converter.convert()

# Check values from converted model.
expected_value = root.assign_add(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
for tf_result, tflite_result in zip(expected_value, actual_value[0]):
    self.assertAllClose(tf_result, tflite_result, atol=1e-05)
