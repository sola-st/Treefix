# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
# The inputs look like this (it's a 3 x 2 matrix, each of depth 2):
#
# [ (1.0, 2.0), (3.0,  4.0), ( 5.0,  6.0) ]
# [ (7.0, 8.0), (9.0, 10.0), (11.0, 12.0) ]
#  We can view this as two inputs
#
#  input depth 0:
#
#  [ 1.0,  3.0,  5.0 ]
#  [ 7.0,  9.0, 11.0 ]
#
#  input depth 1:
#
#  [ 2.0,  4.0,  6.0 ]
#  [ 8.0, 10.0, 12.0 ]
#
# The filter looks like this (it has two 2 x 2 patches, each generating 2
# depths):
#
#  filter #0:
#
#  [ (1.0,  3.0), ( 5.0,  7.0)]
#  [ (9.0, 11.0), (13.0, 15.0)]
#
#  filter #1:
#
#  [ ( 2.0,  4.0), ( 6.0,  8.0)]
#  [ (10.0, 12.0), (14.0, 16.0)]
#
# So the outputs are:
#
# (position 0, 0: in_depth 0, output_depth 0 -- using filter #0)
#  1.0 * 1.0 + 7.0 * 9.0 + 3.0 * 5.0 + 9.0 * 13.0 = 196
# (position 0, 0: in_depth 0, output_depth 1 -- using filter #1)
#  1.0 * 2.0 + 7.0 * 10.0 + 3.0 * 6.0 + 9.0 * 14.0 = 216
# (position 0, 0: in_depth 1, output_depth 2 -- using filter #0)
#  2.0 * 3.0 + 8.0 * 11.0 + 4.0 * 7.0 + 10.0 * 15.0 = 272
# (position 0, 0: in_depth 1, output_depth 3 -- using filter #1)
#  2.0 * 4.0 + 8.0 * 12.0 + 4.0 * 8.0 + 10.0 * 16.0 = 296
#
# (position 1, 0: in_depth 0, output_depth 0 -- using filter #0)
#  3.0 * 1.0 + 9.0 * 9.0 + 5.0 * 5.0 + 11.0 * 13.0 = 252
# (position 1, 0: in_depth 0, output_depth 1 -- using filter #1)
#  3.0 * 2.0 + 9.0 * 10.0 + 5.0 * 6.0 + 11.0 * 14.0 = 280
# (position 1, 0: in_depth 1, output_depth 2 -- using filter #0)
#  4.0 * 3.0 + 10.0 * 11.0 + 6.0 * 7.0 + 12.0 * 15.0 = 344
# (position 1, 0: in_depth 1, output_depth 3 -- using filter #1)
#  4.0 * 4.0 + 10.0 * 12.0 + 6.0 * 8.0 + 12.0 * 16.0 = 376
expected_output = [196, 216, 272, 296, 252, 280, 344, 376]
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 2],
    filter_in_sizes=[2, 2, 2, 2],
    stride=1,
    padding="VALID",
    expected=expected_output)
