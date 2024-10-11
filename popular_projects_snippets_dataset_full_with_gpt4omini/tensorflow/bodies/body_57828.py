# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, func, calibration_gen = self._getIntegerQuantizationModelWithFlexOp()

quantized_converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [func], root)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
if is_int_only:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.
            EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
            lite.OpsSet.SELECT_TF_OPS
        ]
    else:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.TFLITE_BUILTINS_INT8, lite.OpsSet.SELECT_TF_OPS
        ]
else:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.
            EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
            lite.OpsSet.TFLITE_BUILTINS,
            lite.OpsSet.SELECT_TF_OPS
        ]
    else:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.TFLITE_BUILTINS, lite.OpsSet.SELECT_TF_OPS
        ]

quantized_converter.inference_input_type = inference_input_output_type
quantized_converter.inference_output_type = inference_input_output_type
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(quantized_tflite_model)
self.assertIsNotNone(metadata)
self.assertEqual(metadata.options.enableSelectTfOps, True)
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
