# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
"""Iterator for different convolution shapes, strides and paddings.

  Yields:
    Tuple (input_size, filter_size, out_size, stride, dilation, padding), the
    depthwise
    convolution parameters.
  """
input_sizes = [[4, 6, 6, 48], [4, 8, 8, 84], [4, 36, 36, 2], [4, 148, 148, 2],
               [3, 300, 300, 3]]
filter_sizes = [[1, 1, 48, 2], [1, 3, 84, 1], [5, 5, 2, 1], [4, 4, 2, 8],
                [2, 2, 3, 8]]
out_sizes = [[4, 6, 6, 96], [4, 8, 8, 84], [4, 36, 36, 2], [4, 74, 74, 16],
             [3, 296, 296, 24]]
strides = [1, 1, 2, 2, 1]
dilations = [2, 2, 4, 2, 4]
# pylint: disable=invalid-name
VALID = "VALID"
SAME = "SAME"
# pylint: enable=invalid-name
paddings = [SAME, SAME, SAME, SAME, VALID]
for i, f, o, s, d, p in zip(input_sizes, filter_sizes, out_sizes, strides,
                            dilations, paddings):
    exit((i, f, o, s, d, p))
