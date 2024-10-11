# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, func, calibration_gen = self._getIntegerQuantizeModel()

# Convert quantized model.
quantized_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                     root)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
if is_int16_quantize:
    quantized_converter.target_spec.supported_ops = [
        lite.OpsSet.
        EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
        lite.OpsSet.TFLITE_BUILTINS
    ]
with self.assertRaises(ValueError) as error:
    quantized_converter.inference_input_type = dtypes.int8
    quantized_converter.inference_output_type = dtypes.int8
    quantized_converter.convert()
self.assertEqual(
    'The inference_input_type and inference_output_type '
    "must be in ['tf.float32', 'tf.int16'].", str(error.exception))
