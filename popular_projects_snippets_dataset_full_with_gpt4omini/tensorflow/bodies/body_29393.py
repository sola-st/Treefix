# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
in_height = out_height * block_size
in_width = out_width * block_size
nhwc_input_shape = [batch_size, in_height, in_width, in_channels]
nchw_input_shape = [batch_size, in_channels, in_height, in_width]
total_size = np.prod(nhwc_input_shape)

# Construct the input tensor in data_type and NHWC.
# force_cpu is needed because quantize_v2 runs on only CPU.
with test_util.force_cpu():
    if data_type == dtypes.qint8:
        # Initialize the input tensor with qint8 values that circle -127..127.
        x = [((f + 128) % 255) - 127 for f in range(total_size)]
        t = constant_op.constant(
            x, shape=nhwc_input_shape, dtype=dtypes.float32)
        t, _, _ = gen_array_ops.quantize_v2(t, -128.0, 127.0, dtypes.qint8)
    else:
        assert data_type == dtypes.float32
        # Initialize the input tensor with ascending whole numbers as floats.
        x = [f * 1.0 for f in range(total_size)]
        shape = nchw_input_shape if data_format == "NCHW" else nhwc_input_shape
        t = constant_op.constant(x, shape=shape, dtype=dtypes.float32)

with test_util.device(use_gpu):
    if data_format == "NCHW_VECT_C":
        assert data_type == dtypes.qint8

        # Convert to int8, then NHWCToNCHW_VECT_C, and then back to qint8.
        actual = array_ops.bitcast(t, dtypes.int8)
        actual = test_util.NHWCToNCHW_VECT_C(actual)
        actual = array_ops.bitcast(actual, dtypes.qint8)
        actual = array_ops.space_to_depth(
            actual, block_size, data_format=data_format)
        actual = array_ops.bitcast(actual, dtypes.int8)
        actual = test_util.NCHW_VECT_CToNHWC(actual)
        actual = array_ops.bitcast(actual, dtypes.qint8)

        expected = array_ops.bitcast(t, dtypes.int8)
        expected = math_ops.cast(expected, dtypes.float32)
        expected = self.spaceToDepthUsingTranspose(expected, block_size, "NHWC")
        expected = math_ops.cast(expected, dtypes.int8)
        expected = array_ops.bitcast(expected, dtypes.qint8)
    else:
        # Initialize the input tensor with ascending whole numbers as floats.
        actual = array_ops.space_to_depth(
            t, block_size, data_format=data_format)
        expected = self.spaceToDepthUsingTranspose(t, block_size, data_format)

    actual_vals, expected_vals = self.evaluate([actual, expected])
    self.assertTrue(np.array_equal(actual_vals, expected_vals))
