# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root = self._getSimpleVariableModel()
input_data = tf.constant(1., shape=[1])
concrete_func = root.f.get_concrete_function(input_data)

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
tflite_model = converter.convert()

# Check output value from converted model.
expected_value = root.f(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertEqual(expected_value.numpy(), actual_value)
