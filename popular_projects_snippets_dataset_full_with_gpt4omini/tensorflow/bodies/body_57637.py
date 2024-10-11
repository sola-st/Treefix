# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
np.random.seed(0)
with ops.Graph().as_default():
    # We need the tensor to have more than 1024 elements for quantize_weights
    # to kick in. Thus, the [33, 33] shape.
    in_tensor_1 = array_ops.placeholder(
        shape=[33, 33], dtype=dtypes.float32, name='inputA')
    in_tensor_2 = constant_op.constant(
        np.random.uniform(low=-10., high=10., size=(33, 33)),
        shape=[33, 33],
        dtype=dtypes.float32,
        name='inputB')
    out_tensor = math_ops.matmul(in_tensor_1, in_tensor_2, name='output')
    sess = session.Session()

# Attempt to convert to quantized weights model.
quantized_converter = lite.TFLiteConverter.from_session(
    sess, [in_tensor_1], [out_tensor])
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
# Restricting to int8 type only
quantized_converter.target_spec.supported_types = [dtypes.int8]
# A representative dataset is required for full fixed point quantization.
with self.assertRaises(ValueError) as error:
    quantized_converter.convert()
self.assertEqual(
    'For full integer quantization, a `representative_dataset` '
    'must be specified.', str(error.exception))
