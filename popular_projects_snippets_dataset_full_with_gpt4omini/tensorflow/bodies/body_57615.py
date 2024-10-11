# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
k_conv_name = 'Conv2D1'
# Dynamic range quant requires total num elements of filters > 1024.
k_num_filters = 38
with ops.Graph().as_default():
    inp, output, calibration_gen = self._getIntegerQuantizeModel(
        k_num_filters)
    sess = session.Session()

quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
if representative_dataset:
    quantized_converter.representative_dataset = calibration_gen
quantized_converter.experimental_new_quantizer = enable_mlir_quantizer
if disable_per_channel:
    quantized_converter._experimental_disable_per_channel = (
        disable_per_channel)
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
detail = next((d for d in interpreter.get_tensor_details()
               if d['name'] == k_conv_name))
quant_params = detail['quantization_parameters']
expected_num_params = 1 if disable_per_channel else k_num_filters
self.assertLen(quant_params['scales'], expected_num_params)
self.assertLen(quant_params['zero_points'], expected_num_params)
