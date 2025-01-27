# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
from l3.Runtime import _l_
"""Iterator for different convolution shapes, strides and explicit paddings.

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
    _l_(16862)

    aux = (input_size, filter_size, out_size, stride, padding, dilations)
    _l_(16861)
    exit(aux)
aux = [
    Config([4, 5, 5, 48], [1, 1, 48, 2], [4, 8, 12, 96],
           padding=[[1, 2], [3, 4]]),
    Config([4, 1, 1, 3], [3, 3, 3, 2], [4, 29, 39, 6],
           padding=[[10, 20], [15, 25]]),
    Config([4, 9, 27, 8], [3, 3, 8, 1], [4, 14, 31, 8],
           padding=[[3, 4], [4, 2]]),
    Config([4, 31, 31, 7], [3, 3, 7, 1], [4, 29, 29, 7],
           padding=[[0, 0], [0, 0]]),
    Config([3, 299, 299, 3], [3, 2, 3, 8], [3, 150, 153, 24],
           2,
           padding=[[1, 2], [3, 5]]),
    Config([5, 183, 183, 1], [5, 5, 1, 2], [5, 62, 60, 2],
           3,
           padding=[[3, 2], [1, 0]]),
    Config([5, 29, 31, 1], [5, 4, 1, 2], [5, 26, 23, 2],
           padding=[[3, 2], [1, 0]],
           dilations=[2, 3]),
    # These cases test the kernels in depthwise_conv_op_gpu.h which are used
    # if the input size is small.
    Config([4, 5, 5, 48], [3, 3, 48, 1], [4, 5, 5, 48],
           padding=[[0, 2], [0, 2]]),
    Config([1, 8, 7, 2], [8, 7, 2, 1], [1, 8, 7, 2], padding=[[0, 7], [3,
                                                                       3]]),
    Config([2, 4, 3, 2], [3, 2, 2, 1], [2, 4, 3, 2], padding=[[2, 0], [1,
                                                                       0]]),
]
_l_(16863)

exit(aux)
