# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test the model quantized by the new converter and denylisted options."""
root, func, calibration_gen = self._getIntegerQuantizeModel()
quantized_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                     root)
quantized_converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS_INT8
]
quantized_converter.representative_dataset = calibration_gen
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.experimental_new_quantizer = True
quantized_converter._experimental_calibrate_only = True
quantized_converter.experimental_lower_to_saved_model = lower_to_saved_model
calibrated = quantized_converter.convert()
quantized_tflite_model = mlir_quantize(
    calibrated,
    denylisted_ops=denylisted_ops,
    denylisted_nodes=denylisted_nodes)
interpreter = Interpreter(model_content=quantized_tflite_model)
details = interpreter.get_tensor_details()
num_quantized_tensors = sum(
    [1 for detail in details
     if len(detail['quantization_parameters']['scales'])])
if denylisted_nodes or denylisted_ops:
    self.assertEqual(num_quantized_tensors, 0)
    exit()
self.assertEqual(num_quantized_tensors, 4)  # quant, filter, bias, dequant
