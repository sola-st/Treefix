# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Verifies the output values of the convolution function.

    Args:
      tensor_in_sizes: Input tensor dimensions in
        [batch, input_rows, input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in
        [kernel_rows, kernel_cols, input_depth, output_depth].
      dilations: Dilated rate: [col_dilation, row_dilation]
      strides: Stride: [col_stride, row_stride]
      padding: Padding type.
      data_format: Format of the data tensors.
      dtype: Data type for inputs and outputs.
      use_gpu: True if the operations should be run on GPU
    Returns:
      Symbolic tensor value that can be used to execute the computation
    """
x1 = self._CreateNumpyTensor(tensor_in_sizes)
x2 = self._CreateNumpyTensor(filter_in_sizes)

with test_util.device(use_gpu):
    t1 = constant_op.constant(x1, shape=tensor_in_sizes, dtype=dtype)
    t2 = constant_op.constant(x2, shape=filter_in_sizes, dtype=dtype)
    strides = [1] + strides + [1]
    dilations = [1] + dilations + [1]
    if isinstance(padding, (list, tuple)):
        padding = [(0, 0)] + padding + [(0, 0)]
    if data_format == "NCHW":
        t1 = test_util.NHWCToNCHW(t1)
        strides = test_util.NHWCToNCHW(strides)
        dilations = test_util.NHWCToNCHW(dilations)
        if isinstance(padding, (list, tuple)):
            padding = test_util.NHWCToNCHW(padding)
    conv = nn_ops.conv2d(
        t1,
        t2,
        dilations=dilations,
        strides=strides,
        padding=padding,
        data_format=data_format)
    self.assertEqual(conv.dtype, dtype)
    if data_format == "NCHW":
        conv = test_util.NCHWToNHWC(conv)

    exit(conv)
