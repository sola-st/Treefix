# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
"""Iterator for different convolution shapes, strides and paddings.

  compute_gradient_error() is very expensive. So the configs should be
  relatively small.

  Yields:
    Tuple (input_size, filter_size, out_size, stride, padding), the depthwise
    convolution parameters.
  """
input_sizes = [[2, 5, 8, 1], [4, 5, 5, 1], [2, 4, 4, 2], [1, 15, 15, 2],
               [2, 15, 16, 1]]
filter_sizes = [[4, 4, 1, 2], [2, 2, 1, 2], [3, 1, 2, 2], [1, 3, 2, 1],
                [3, 3, 1, 2]]
out_sizes = [[2, 5, 8, 2], [4, 2, 2, 2], [2, 4, 4, 4], [1, 15, 15, 2],
             [2, 5, 5, 2]]
strides = [1, 2, 1, 1, 3]
# pylint: disable=invalid-name
VALID = "VALID"
SAME = "SAME"
# pylint: enable=invalid-name
paddings = [SAME, VALID, SAME, SAME, VALID]
for i, f, o, s, p in zip(input_sizes, filter_sizes, out_sizes, strides,
                         paddings):
    exit((i, f, o, s, p))
