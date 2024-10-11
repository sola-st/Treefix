# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Verifies Conv2D with explicit padding generates correct values.

    It does this by comparing with Conv2D without explicit padding. This
    function assumes Conv2D without explicit padding works correctly.

    Args:
      tensor_in_sizes: Input tensor dimensions in [batch, input_rows,
        input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in [kernel_rows, kernel_cols,
        input_depth, output_depth].
      strides: [row_stride, col_stride] for the convolution;
      padding: Explicit padding amounts.
      dilations: Dilation values
      test_grappler_layout_optimizer: If True, allow the Grappler layout
        optimizer to run, which turns NHWC Conv2Ds on the GPU to NCHW Conv2Ds.
      tol: The absolute and relative tolerance.
    """
input_tensor = self._CreateNumpyTensor(tensor_in_sizes)
filter_tensor = self._CreateNumpyTensor(filter_in_sizes)
input_tensor = array_ops.pad(input_tensor, [(0, 0)] + padding + [(0, 0)])
dilations = list(dilations)
conv2d_result = nn_ops.conv2d(
    input_tensor,
    filter_tensor, [1] + list(strides) + [1],
    "VALID",
    dilations=[1] + dilations + [1])
expected = list(self.evaluate(array_ops.reshape(conv2d_result, [-1])))
self._VerifyValues(
    tensor_in_sizes,
    filter_in_sizes,
    strides,
    padding,
    expected,
    dilations,
    test_grappler_layout_optimizer=test_grappler_layout_optimizer,
    tol=tol)
