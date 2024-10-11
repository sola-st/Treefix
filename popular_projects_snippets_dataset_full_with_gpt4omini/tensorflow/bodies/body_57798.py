# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Convert a single model in a multi-functional model."""
root = self._getMultiFunctionModel()
input_data = tf.constant(1., shape=[1])
concrete_func = root.add.get_concrete_function(input_data)

# Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = root.add(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertEqual(expected_value.numpy(), actual_value)
