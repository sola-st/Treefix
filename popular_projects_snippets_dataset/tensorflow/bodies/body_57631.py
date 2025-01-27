# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[33, 33], dtype=dtypes.float32, name='inputA')
    in_tensor_2 = constant_op.constant(
        np.random.uniform(low=-10., high=10., size=(33, 33)),
        shape=[33, 33],
        dtype=dtypes.float32,
        name='inputB')
    out_tensor = math_ops.matmul(in_tensor_1, in_tensor_2, name='output')
    sess = session.Session()

quantized_converter = lite.TFLiteConverter.from_session(
    sess, [in_tensor_1], [out_tensor])
self.assertFalse(quantized_converter.post_training_quantize)

quantized_converter.post_training_quantize = True
self.assertTrue(quantized_converter.post_training_quantize)
self.assertEqual(quantized_converter.optimizations, [lite.Optimize.DEFAULT])

quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)
