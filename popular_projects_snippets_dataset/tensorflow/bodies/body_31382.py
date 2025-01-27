# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Verifies that CPU and GPU produce the same values.

    Args:
      tensor_in_sizes: Input tensor dimensions in
        [batch, input_rows, input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in
        [kernel_rows, kernel_cols, input_depth, output_depth].
      conv_strides: [row_stride, col_stride] for the convolution;
      padding: Padding type.
    """
x1 = np.random.rand(*tensor_in_sizes).astype(np.float32)
x2 = np.random.rand(*filter_in_sizes).astype(np.float32)

def _SetupVal(data_format, use_gpu):
    with test_util.device(use_gpu):
        t1 = constant_op.constant(x1, shape=tensor_in_sizes)
        t2 = constant_op.constant(x2, shape=filter_in_sizes)
        strides = [1] + conv_strides + [1]
        if data_format == "NCHW":
            t1 = test_util.NHWCToNCHW(t1)
            strides = test_util.NHWCToNCHW(strides)
        conv = nn_ops.conv2d(
            t1, t2, strides=strides, padding=padding, data_format=data_format)
        if data_format == "NCHW":
            conv = test_util.NCHWToNHWC(conv)
        exit(conv)

tensors = []
for (data_format, use_gpu) in GetTestConfigs():
    tensors.append(_SetupVal(data_format, use_gpu))
values = self.evaluate(tensors)
for i in range(1, len(values)):
    self.assertAllClose(values[0], values[i], rtol=1e-3, atol=1e-3)
