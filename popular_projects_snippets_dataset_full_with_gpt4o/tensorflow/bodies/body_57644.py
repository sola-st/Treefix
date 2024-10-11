# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    inp, output, calibration_gen = self._getIntegerQuantizeModel()
    sess = session.Session()

# Convert float model.
float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)

converter = lite.TFLiteConverter.from_session(sess, [inp], [output])

# extra flags to trigger training time quantization conversion
converter.inference_type = dtypes.int8
converter.inference_input_type = dtypes.float32
converter.inference_output_type = dtypes.float32
input_arrays = converter.get_input_arrays()
converter.quantized_input_stats = {input_arrays[0]: (0., 1.)}
# trigger post-training quantization
converter.optimizations = [lite.Optimize.DEFAULT]
converter.representative_dataset = calibration_gen
converter.experimental_new_quantizer = True
quantized_tflite_model = converter.convert()
self.assertIsNotNone(quantized_tflite_model)
self.assertLess(len(quantized_tflite_model), len(float_tflite_model))

# calibration only api
converter._experimental_calibrate_only = True
calibrated_tflite = converter.convert()
quantized_tflite_model = mlir_quantize(
    calibrated_tflite, fully_quantize=True)
interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
self.assertEqual(np.int8, input_details[0]['dtype'])
self.assertEqual((1., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertEqual(np.int8, output_details[0]['dtype'])
