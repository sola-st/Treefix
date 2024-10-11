# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, func, calibration_gen = self._getIntegerQuantizeModel()

# Convert float model.
float_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                 root)
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)

converter = lite.TFLiteConverterV2.from_concrete_functions([func], root)
# TODO(b/156309549): We should add INT16 to the builtin types.
converter.optimizations = [lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [
    lite.OpsSet.EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
]
converter.representative_dataset = calibration_gen
# TODO(b/175659372): We should support 16x8 mode in the mlir quantizer
# converter._experimental_calibrate_only = True
# calibrated_tflite = converter.convert()
# quantized_tflite_model = mlir_quantize(
#     calibrated_tflite, inference_type=_types_pb2.QUANTIZED_INT16)
quantized_tflite_model = converter.convert()

self.assertIsNotNone(quantized_tflite_model)

# The default input and output types should be float.
interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual(np.float32, input_details[0]['dtype'])
output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(np.float32, output_details[0]['dtype'])

# The weights tensor should be quantized to 8 bits,
# the bias tensor should be 32 bits to utilize optimized kernels,
# and the activations should be 16 bits.
tensor_details = interpreter.get_tensor_details()
# TODO(b/175659372): The old quantizer yields a 64 bit bias and a
# slightly different tensor order than the new one.
# self.assertEqual(np.int8, tensor_details[1]['dtype'])
# self.assertEqual(np.int32, tensor_details[0]['dtype'])
# self.assertEqual(np.int16, tensor_details[2]['dtype'])
# self.assertEqual(np.int16, tensor_details[3]['dtype'])
self.assertEqual(np.int8, tensor_details[2]['dtype'])
self.assertEqual(np.int64, tensor_details[1]['dtype'])
self.assertEqual(np.int16, tensor_details[0]['dtype'])
self.assertEqual(np.int16, tensor_details[3]['dtype'])

# Ensure that the quantized weights tflite model is smaller.
self.assertLess(len(quantized_tflite_model), len(float_tflite_model))
