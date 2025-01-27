# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
k_conv_name = 'Conv2D'
# Dynamic range quant requires total num elements of filters > 1024.
k_num_filters = 38
root, func, calib_gen = self._getIntegerQuantizeModel(k_num_filters)
quantized_converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [func], root)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calib_gen
quantized_converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS
]
quantized_converter.experimental_new_quantizer = enable_mlir_quantizer
if disable_per_channel:
    quantized_converter._experimental_disable_per_channel = (
        disable_per_channel)
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
detail = next((d for d in interpreter.get_tensor_details()
               if d['name'].startswith(k_conv_name)))
quant_params = detail['quantization_parameters']
expected_num_params = 1 if disable_per_channel else k_num_filters
self.assertLen(quant_params['scales'], expected_num_params)
self.assertLen(quant_params['zero_points'], expected_num_params)
