# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, func, calib_gen = self._getIntegerQuantizationModelWithControlFlow()

quantized_converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [func], root)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calib_gen
if is_int_only:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet
            .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
            lite.OpsSet.TFLITE_BUILTINS
        ]
    else:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.TFLITE_BUILTINS_INT8, lite.OpsSet.TFLITE_BUILTINS
        ]
else:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet
            .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
            lite.OpsSet.TFLITE_BUILTINS
        ]
    else:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.TFLITE_BUILTINS
        ]

quantized_converter.inference_input_type = inference_input_output_type
quantized_converter.inference_output_type = inference_input_output_type
quantized_converter.experimental_new_quantizer = enable_mlir_quantizer

quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

expected_dtype = inference_input_output_type.as_numpy_dtype

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertEqual(input_details[0]['dtype'], expected_dtype)
self.assertEqual(input_details[1]['dtype'], dtypes.bool)
output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(output_details[0]['dtype'], expected_dtype)
