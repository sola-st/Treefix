# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
"""Iterator for different convolution shapes, strides and paddings.

  Yields:
    Tuple (input_size, filter_size, out_size, stride, padding), the depthwise
    convolution parameters.
  """
input_sizes = [[4, 5, 5, 48], [2, 5, 5, 48], [4, 8, 8, 84], [4, 17, 17, 48],
               [4, 9, 27, 8], [4, 31, 31, 7], [4, 35, 35, 2],
               [4, 147, 147, 2], [3, 299, 299, 3], [5, 183, 183, 1]]
filter_sizes = [[1, 1, 48, 2], [2, 2, 48, 8], [1, 3, 84, 1], [3, 1, 48, 4],
                [3, 3, 8, 1], [3, 3, 7, 1], [5, 5, 2, 1], [3, 3, 2, 8],
                [2, 2, 3, 8], [5, 5, 1, 2]]
out_sizes = [[4, 5, 5, 96], [2, 5, 5, 384], [4, 8, 8, 84], [4, 17, 17, 192],
             [4, 9, 27, 8], [4, 31, 31, 7], [4, 35, 35, 2], [4, 49, 49, 16],
             [3, 150, 150, 24], [5, 92, 92, 2]]
strides = [1, 1, 1, 1, 1, 1, 1, 3, 2, 2]
# pylint: disable=invalid-name
VALID = "VALID"
SAME = "SAME"
# pylint: enable=invalid-name
paddings = [SAME, SAME, SAME, SAME, SAME, SAME, SAME, VALID, SAME, SAME, SAME]
for i, f, o, s, p in zip(input_sizes, filter_sizes, out_sizes, strides,
                         paddings):
    exit((i, f, o, s, p))
