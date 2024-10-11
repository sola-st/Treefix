# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = array_ops.fake_quant_with_min_max_args(
        in_tensor + in_tensor, min=0., max=1.)
    sess = session.Session()

quantized_converter = lite.TFLiteConverter.from_session(
    sess, [in_tensor], [out_tensor])

with self.assertRaises(ValueError) as error:
    quantized_converter.inference_type = quantized_type
    quantized_converter.convert()
self.assertEqual(
    'The `quantized_input_stats` flag must be defined when either '
    '`inference_type` flag or `inference_input_type` flag is set to '
    'tf.int8 or tf.uint8. Currently, `inference_type=tf.{}` and '
    '`inference_input_type=None`.'.format(quantized_type.name),
    str(error.exception))

with self.assertRaises(ValueError) as error:
    quantized_converter.inference_type = dtypes.float32
    quantized_converter.inference_input_type = quantized_type
    quantized_converter.convert()
self.assertEqual(
    'The `quantized_input_stats` flag must be defined when either '
    '`inference_type` flag or `inference_input_type` flag is set to '
    'tf.int8 or tf.uint8. Currently, `inference_type=tf.float32` and '
    '`inference_input_type=tf.{}`.'.format(quantized_type.name),
    str(error.exception))

quantized_converter.inference_type = quantized_type
quantized_converter.inference_input_type = quantized_type

input_arrays = quantized_converter.get_input_arrays()
quantized_converter.quantized_input_stats = {input_arrays[0]: (0., 1.)}
quantized_converter.convert()
