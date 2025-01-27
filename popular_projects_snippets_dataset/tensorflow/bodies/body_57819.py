# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
model = self._getTrainingTimeQuantizedModel()

float_converter = lite.TFLiteConverterV2.from_keras_model(model)
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)

quantized_converter = lite.TFLiteConverterV2.from_keras_model(model)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.inference_input_type = inference_input_output_type
quantized_converter.inference_output_type = inference_input_output_type
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(quantized_tflite_model)
self.assertIsNotNone(metadata)
self.assertAllEqual(
    [metadata_fb.ModelOptimizationMode.QUANTIZATION_AWARE_TRAINING],
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

# Ensure that the quantized tflite model is smaller.
self.assertLess(len(quantized_tflite_model), len(float_tflite_model))
