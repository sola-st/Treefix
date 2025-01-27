# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name='inputA')
    in_tensor_2 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name='inputB')
    out_tensor = array_ops.fake_quant_with_min_max_args(
        in_tensor_1 + in_tensor_2, min=0., max=1., name='output')
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess,
                                              [in_tensor_1, in_tensor_2],
                                              [out_tensor])
converter.inference_type = dtypes.uint8
converter.quantized_input_stats = {'inputA': (0., 1.)}  # mean, std_dev
with self.assertRaises(ValueError) as error:
    converter.convert()
self.assertEqual(
    'Quantization input stats are not available for input tensors '
    '\'inputB\'.', str(error.exception))
