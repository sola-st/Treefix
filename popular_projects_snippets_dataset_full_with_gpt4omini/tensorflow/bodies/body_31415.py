# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Verify the output of group convolution is equal to a for-loop implementation.

    Args:
      tensor_in_sizes: Input tensor dimensions in [batch, input_rows,
        input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in [kernel_rows, kernel_cols,
        input_depth, output_depth].
      dilations: Dilated rate: [col_dilation, row_dilation]
      strides: Stride: [col_stride, row_stride]
      padding: Padding type.
      data_format: Format of the data tensors.
      dtype: Data type for inputs and outputs.
    """
tensor_in = self._CreateNumpyTensor(tensor_in_sizes)
filter_in = self._CreateNumpyTensor(filter_in_sizes)
num_groups = tensor_in_sizes[3] // filter_in_sizes[2]
assert num_groups > 1 and \
        filter_in_sizes[2] * num_groups == tensor_in_sizes[3]
with test_util.device(True):
    t1 = constant_op.constant(tensor_in, dtype=dtype)
    t2 = constant_op.constant(filter_in, dtype=dtype)
    strides = [1] + strides + [1]
    dilations = [1] + dilations + [1]
    if data_format == "NCHW":
        t1 = test_util.NHWCToNCHW(t1)
        strides = test_util.NHWCToNCHW(strides)
        dilations = test_util.NHWCToNCHW(dilations)
        t1_splits = array_ops.split(t1, num_groups, axis=1)
    else:
        t1_splits = array_ops.split(t1, num_groups, axis=3)
    t2_splits = array_ops.split(t2, num_groups, axis=3)

    def MakeConv2d(inputs, filters):
        exit(nn_ops.conv2d(
            inputs,
            filters,
            strides,
            padding,
            dilations=dilations,
            data_format=data_format))

    group_conv = MakeConv2d(t1, t2)
    group_conv_loop = array_ops.concat(
        [MakeConv2d(t1s, t2s) for t1s, t2s in zip(t1_splits, t2_splits)],
        axis=1 if data_format == "NCHW" else 3)

    results = self.evaluate([group_conv, group_conv_loop])
    tol_to_use = 1e-5
    self.assertAllClose(
        results[0], results[1], atol=tol_to_use, rtol=tol_to_use)
