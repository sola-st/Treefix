# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test the model quantized by the new converter."""
root, func, calibration_gen = self._getIntegerQuantizeModel()

quantized_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                     root)
quantized_converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS_INT8
]
quantized_converter.representative_dataset = calibration_gen

# default quantizer
quantized_converter.experimental_new_quantizer = False
old_tflite = quantized_converter.convert()

# new quantizer
quantized_converter.experimental_new_quantizer = True
new_tflite = quantized_converter.convert()

for _ in range(5):
    input_data = tf.constant(
        np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32))
    old_value = self._evaluateTFLiteModel(old_tflite, [input_data])
    new_value = self._evaluateTFLiteModel(new_tflite, [input_data])
    self.assertAllClose(old_value, new_value, atol=1e-01)
