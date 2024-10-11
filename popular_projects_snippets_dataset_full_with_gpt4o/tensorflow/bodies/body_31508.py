# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Verifies that DeepConv2D and Conv2D produce the same values.

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

with self.cached_session(use_gpu=False):
    t1 = constant_op.constant(x1, shape=tensor_in_sizes)
    t2 = constant_op.constant(x2, shape=filter_in_sizes)
    strides = [1] + conv_strides + [1]

    conv = nn_ops.conv2d(t1, t2, strides=strides, padding=padding)

    os.environ["TF_USE_DEEP_CONV2D"] = "0"
    values_expect = self.evaluate([conv])

    os.environ["TF_USE_DEEP_CONV2D"] = "1"
    values_test = self.evaluate([conv])

    self.assertAllClose(values_expect, values_test, rtol=1e-5, atol=1e-5)
