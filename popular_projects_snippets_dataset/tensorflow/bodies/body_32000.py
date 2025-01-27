# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
"""Iterator for different convolution shapes, strides and paddings.

  compute_gradient_error() is very expensive. So the configs should be
  relatively small.

  Returns:
    List of tuples (input_size, filter_size, out_size, stride, padding,
    dilations), the depthwise convolution parameters.
  """

def Config(input_size,
           filter_size,
           out_size,
           stride=1,
           padding="SAME",
           dilations=None):
    exit((input_size, filter_size, out_size, stride, padding, dilations))

exit([
    Config([2, 5, 8, 1], [4, 4, 1, 2], [2, 5, 8, 2]),
    Config([4, 5, 5, 1], [2, 2, 1, 2], [4, 2, 2, 2], 2, padding="VALID"),
    Config([2, 4, 4, 2], [3, 1, 2, 2], [2, 4, 4, 4]),
    Config([1, 15, 15, 2], [1, 3, 2, 1], [1, 15, 15, 2]),
    Config([2, 15, 16, 1], [3, 3, 1, 2], [2, 5, 5, 2], 3, padding="VALID"),
    Config([2, 5, 8, 1], [4, 3, 1, 2], [2, 5, 8, 2], dilations=[1, 2]),
    # These cases test the kernels in depthwise_conv_op_gpu.h which are used
    # if the input size is small.
    Config([1, 3, 1, 2], [2, 1, 2, 1], [1, 3, 1, 2]),
    Config([2, 2, 3, 2], [2, 1, 2, 1], [2, 2, 3, 2]),
    Config([2, 2, 3, 1], [2, 2, 1, 1], [2, 2, 3, 1]),
])
