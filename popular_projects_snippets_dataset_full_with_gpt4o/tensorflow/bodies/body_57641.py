# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    inp, output, _ = self._getIntegerQuantizeModel()
    sess = session.Session()

# Specify float16 quantization
quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.target_spec.supported_types = [dtypes.float16]
# Specify only int8 builtin ops
quantized_converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS_INT8
]
with self.assertRaises(ValueError) as error:
    quantized_converter.convert()
self.assertEqual(
    'As full integer quantization has been enabled by setting '
    '`target_spec.supported_ops`={tf.lite.OpsSet.TFLITE_BUILTINS_INT8}, '
    'thus `target_spec.supported_types` should be left uninitizalized '
    'or set to {tf.int8}.', str(error.exception))
