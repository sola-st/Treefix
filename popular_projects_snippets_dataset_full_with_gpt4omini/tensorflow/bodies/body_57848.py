# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root = self._getSimpleVariableModel()
input_data = tf.constant(1., shape=[1])
concrete_func = root.f.get_concrete_function(input_data)

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter.exclude_conversion_metadata = True
tflite_model = converter.convert()
# Check the conversion metadata.
metadata = get_conversion_metadata(tflite_model)
self.assertIsNone(metadata)
