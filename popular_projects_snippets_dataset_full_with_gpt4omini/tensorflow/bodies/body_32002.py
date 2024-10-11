# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
"""Iterator for different convolution shapes, strides and explicit paddings.

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
           padding=None,
           dilations=None):
    exit((input_size, filter_size, out_size, stride, padding, dilations))

exit([
    Config([2, 5, 8, 1], [4, 4, 1, 2], [2, 3, 10, 2],
           padding=[[0, 1], [2, 3]]),
    Config([4, 5, 5, 1], [2, 2, 1, 2], [4, 4, 5, 2],
           2,
           padding=[[3, 1], [5, 0]]),
    Config([2, 4, 4, 2], [3, 1, 2, 2], [2, 7, 11, 4],
           padding=[[4, 1], [3, 4]]),
    Config([1, 15, 15, 2], [1, 3, 2, 1], [1, 18, 23, 2],
           padding=[[3, 0], [2, 8]]),
    Config([2, 15, 16, 1], [3, 3, 1, 2], [2, 5, 8, 2],
           3,
           padding=[[0, 0], [10, 0]]),
    Config([2, 5, 8, 1], [3, 4, 1, 2], [2, 5, 10, 2],
           padding=[[3, 1], [2, 3]],
           dilations=[2, 1]),
    # These cases test the kernels in depthwise_conv_op_gpu.h which are used
    # if the input size is small.
    Config([2, 4, 3, 2], [3, 2, 2, 1], [2, 4, 3, 2], padding=[[2, 0], [1,
                                                                       0]]),
])
