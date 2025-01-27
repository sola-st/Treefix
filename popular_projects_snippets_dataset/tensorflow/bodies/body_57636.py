# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    inp, output, calibration_gen = self._getIntegerQuantizeModel()
    sess = session.Session()

# Convert float model.
float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)

# Convert quantized weights model.
quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])
quantized_converter.inference_input_type = dtypes.int8
quantized_converter.inference_output_type = dtypes.int8
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

# The input and output types should be int8.
interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual(np.int8, input_details[0]['dtype'])
output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(np.int8, output_details[0]['dtype'])

# Ensure that the quantized weights tflite model is smaller.
self.assertLess(len(quantized_tflite_model), len(float_tflite_model))
