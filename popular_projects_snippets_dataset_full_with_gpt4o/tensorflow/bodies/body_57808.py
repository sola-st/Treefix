# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, func, calibration_gen = self._getIntegerQuantizeModel()

# Convert float model.
converter = lite.TFLiteConverterV2.from_concrete_functions([func], root)
tflite_model = converter.convert()
self.assertTrue(tflite_model)

# Convert quantized model.
quantized_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                     root)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
if is_int_only:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.
            EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
        ]
    else:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.TFLITE_BUILTINS_INT8
        ]
else:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.
            EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
            lite.OpsSet.TFLITE_BUILTINS
        ]
quantized_converter.inference_input_type = inference_input_output_type
quantized_converter.inference_output_type = inference_input_output_type
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(quantized_tflite_model)
self.assertIsNotNone(metadata)
expected_opt_options = [metadata_fb.ModelOptimizationMode.PTQ_FULL_INTEGER]
if is_int16_quantize:
    expected_opt_options = [metadata_fb.ModelOptimizationMode.PTQ_INT16]
self.assertAllEqual(expected_opt_options,
                    metadata.options.modelOptimizationModes)

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual(inference_input_output_type.as_numpy_dtype,
                 input_details[0]['dtype'])
output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(inference_input_output_type.as_numpy_dtype,
                 output_details[0]['dtype'])

# Ensure that the quantized tflite model is smaller.
self.assertLess(len(quantized_tflite_model), len(tflite_model))
