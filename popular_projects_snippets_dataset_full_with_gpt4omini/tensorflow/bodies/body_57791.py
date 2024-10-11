# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root = self._getSimpleVariableModel()
input_data = tf.constant(1., shape=[1])
concrete_func = root.f.get_concrete_function(input_data)

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
with self.assertRaises(ValueError) as error:
    converter.inference_input_type = inference_input_output_type
    converter.inference_output_type = inference_input_output_type
    converter.convert()
self.assertEqual(
    'The inference_input_type and inference_output_type '
    'must be tf.float32.', str(error.exception))
