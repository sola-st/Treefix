# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, func, _ = self._getIntegerQuantizeModel()

# Convert float model.
converter = lite.TFLiteConverterV2.from_concrete_functions([func], root)
tflite_model = converter.convert()
self.assertTrue(tflite_model)

# Convert quantized model.
quantized_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                     root)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
with self.assertRaises(ValueError) as error:
    quantized_converter.inference_input_type = inference_input_output_type
    quantized_converter.inference_output_type = inference_input_output_type
    quantized_converter.convert()
self.assertEqual(
    'The inference_input_type and inference_output_type '
    'must be tf.float32.', str(error.exception))
