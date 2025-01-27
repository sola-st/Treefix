# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
"""Tests that tf.nn.conv2d produces the expected value.

    Args:
      input_sizes: Input tensor dimensions in
        [batch, input_rows, input_cols, input_depth].
      filter_sizes: Filter tensor dimensions in
        [kernel_rows, kernel_cols, input_depth, output_depth].
      strides: Strides.
      dilations: RHS dilations.
      padding: Padding type.
      data_format_src: Data format input is in.
      data_format_dst: Data format verification will run and input is converted
        to.
      expected: Expected output.
    """

total_size_1 = np.prod(input_sizes)
total_size_2 = np.prod(filter_sizes)
x1 = np.arange(1, total_size_1 + 1, dtype=np.float32).reshape(input_sizes)
x2 = np.arange(1, total_size_2 + 1, dtype=np.float32).reshape(filter_sizes)
strides = [1] + strides + [1]
if dilations is None:
    dilations = [1, 1]
dilations = [1] + dilations + [1]

# Convert between data formats.
expected = test_utils.ConvertBetweenDataFormats(expected, data_format_src,
                                                data_format_dst)
x1 = test_utils.ConvertBetweenDataFormats(x1, data_format_src,
                                          data_format_dst)
input_sizes = test_utils.PermuteDimsBetweenDataFormats(
    input_sizes, data_format_src, data_format_dst)
strides = test_utils.PermuteDimsBetweenDataFormats(strides, data_format_src,
                                                   data_format_dst)
dilations = test_utils.PermuteDimsBetweenDataFormats(
    dilations, data_format_src, data_format_dst)

with self.session() as sess:
    t1 = array_ops.placeholder(dtypes.float32, shape=input_sizes)
    t2 = array_ops.placeholder(dtypes.float32, shape=filter_sizes)
    with self.test_scope():
        out = nn_ops.conv2d(
            t1,
            t2,
            strides=strides,
            padding=padding,
            data_format=data_format_dst,
            dilations=dilations)

    value = sess.run(out, {t1: x1, t2: x2})
    self.assertAllClose(expected, value, 1e-3)
