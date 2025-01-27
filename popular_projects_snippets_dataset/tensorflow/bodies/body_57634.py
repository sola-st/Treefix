# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    inp, output, calibration_gen = self._getIntegerQuantizeModel()
    sess = session.Session()

# Convert float model.
float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(float_tflite_model)
self.assertIsNotNone(metadata)
self.assertEqual(
    metadata.environment.tensorflowVersion.decode('utf-8'),
    versions.__version__)
self.assertEqual(metadata.environment.apiVersion, 1)
self.assertEqual(metadata.environment.modelType,
                 metadata_fb.ModelType.TF_SESSION)
self.assertEqual(metadata.options.allowCustomOps, False)
self.assertEqual(metadata.options.enableSelectTfOps, False)
self.assertEqual(metadata.options.forceSelectTfOps, False)
self.assertAllEqual([], metadata.options.modelOptimizationModes)

# Convert quantized model.
quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(quantized_tflite_model)
self.assertIsNotNone(metadata)
self.assertAllEqual([metadata_fb.ModelOptimizationMode.PTQ_FULL_INTEGER],
                    metadata.options.modelOptimizationModes)

# The default input and output types should be float.
interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual(np.float32, input_details[0]['dtype'])
output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(np.float32, output_details[0]['dtype'])

# Ensure that the quantized weights tflite model is smaller.
self.assertLess(len(quantized_tflite_model), len(float_tflite_model))
