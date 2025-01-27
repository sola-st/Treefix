# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
"""Tests that gen_nn_ops.conv2d_backprop_filter produces the right output.

    Args:
      input_sizes: Input tensor dimensions in
        [batch, input_rows, input_cols, input_depth].
      filter_sizes: Filter tensor dimensions in
        [kernel_rows, kernel_cols, input_depth, output_depth].
      out_backprop_sizes: Output gradients tensor dimensions.
      strides: Stride.
      dilations: Dilations.
      padding: Padding type.
      data_format_src: Data format input is in.
      data_format_dst: Data format verification will run and input is converted
        to.
      expected: Expected output.
    """

total_size_1 = np.prod(input_sizes)
total_size_2 = np.prod(out_backprop_sizes)
x1 = np.arange(1, total_size_1 + 1, dtype=np.float32).reshape(input_sizes)
x2 = np.arange(
    1, total_size_2 + 1, dtype=np.float32).reshape(out_backprop_sizes)
strides = [1] + strides + [1]
if dilations is not None:
    dilations = [1] + dilations + [1]

expected = np.reshape(expected, filter_sizes)

# Convert between data formats.
x1 = test_utils.ConvertBetweenDataFormats(x1, data_format_src,
                                          data_format_dst)
x2 = test_utils.ConvertBetweenDataFormats(x2, data_format_src,
                                          data_format_dst)
input_sizes = test_utils.PermuteDimsBetweenDataFormats(
    input_sizes, data_format_src, data_format_dst)
out_backprop_sizes = test_utils.PermuteDimsBetweenDataFormats(
    out_backprop_sizes, data_format_src, data_format_dst)
strides = test_utils.PermuteDimsBetweenDataFormats(strides, data_format_src,
                                                   data_format_dst)
if dilations is not None:
    dilations = test_utils.PermuteDimsBetweenDataFormats(
        dilations, data_format_src, data_format_dst)

with self.session() as sess:
    t1 = array_ops.placeholder(dtypes.float32, shape=input_sizes)
    t2 = array_ops.placeholder(dtypes.float32, shape=out_backprop_sizes)
    with self.test_scope():
        tensor = gen_nn_ops.conv2d_backprop_filter(
            input=t1,
            filter_sizes=filter_sizes,
            out_backprop=t2,
            strides=strides,
            dilations=dilations,
            padding=padding,
            data_format=data_format_dst)

    value = sess.run(tensor, {t1: x1, t2: x2})
    self.assertAllEqual(filter_sizes, value.shape)
    self.assertAllClose(expected, value, 1e-3)
