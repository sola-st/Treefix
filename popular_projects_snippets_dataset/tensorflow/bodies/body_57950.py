# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, concrete_func, calibration_gen = (
    self._getIntegerQuantizeModelWithUnknownShapes())
float_converter = lite.TFLiteConverterV2.from_concrete_functions(
    [concrete_func], root)
float_tflite_model = float_converter.convert()

quantized_converter = lite.TFLiteConverterV2.from_concrete_functions(
    [concrete_func], root)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
quantized_tflite_model = quantized_converter.convert()

# The default input and output types should be float.
quantized_interpreter = Interpreter(model_content=quantized_tflite_model)
quantized_interpreter.allocate_tensors()
input_details = quantized_interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([-1, 33], input_details[0]['shape_signature'])

# Ensure that the quantized weights tflite model is smaller.
self.assertLess(len(quantized_tflite_model), len(float_tflite_model))
