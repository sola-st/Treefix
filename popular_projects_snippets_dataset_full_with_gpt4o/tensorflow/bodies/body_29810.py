# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
in_channels = out_channels * block_size * block_size
nhwc_input_shape = [batch_size, in_height, in_width, in_channels]
nchw_input_shape = [batch_size, in_channels, in_height, in_width]
total_size = np.prod(nhwc_input_shape)

if data_format == "NCHW_VECT_C":
    # Initialize the input tensor with qint8 values that circle -127..127.
    x = [((f + 128) % 255) - 127 for f in range(total_size)]
    t = constant_op.constant(x, shape=nhwc_input_shape, dtype=dtypes.float32)
    expected = self.depthToSpaceUsingTranspose(t, block_size, "NHWC")
    t = test_util.NHWCToNCHW_VECT_C(t)
    t, _, _ = gen_array_ops.quantize_v2(t, -128.0, 127.0, dtypes.qint8)
    t = array_ops.depth_to_space(t, block_size, data_format="NCHW_VECT_C")
    t = gen_array_ops.dequantize(t, -128, 127)
    actual = test_util.NCHW_VECT_CToNHWC(t)
else:
    # Initialize the input tensor with ascending whole numbers as floats.
    x = [f * 1.0 for f in range(total_size)]
    shape = nchw_input_shape if data_format == "NCHW" else nhwc_input_shape
    t = constant_op.constant(x, shape=shape, dtype=dtypes.float32)
    expected = self.depthToSpaceUsingTranspose(t, block_size, data_format)
    actual = array_ops.depth_to_space(t, block_size, data_format=data_format)

with self.session(use_gpu=use_gpu) as sess:
    actual_vals, expected_vals = self.evaluate([actual, expected])
    self.assertTrue(np.array_equal(actual_vals, expected_vals))
