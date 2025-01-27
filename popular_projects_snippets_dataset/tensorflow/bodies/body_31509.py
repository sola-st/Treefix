# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
input_sizes = [[5, 5, 5, 1248], [3, 17, 17, 192], [2, 35, 35, 288],
               [2, 6, 8, 517], [2, 7, 4, 81], [3, 11, 3, 77]]
filter_sizes = [[3, 3, 1248, 128], [3, 3, 192, 192], [3, 3, 288, 384],
                [3, 3, 517, 64], [3, 3, 81, 77], [3, 3, 77, 181]]
for input_shape, filter_shape in zip(input_sizes, filter_sizes):
    self._CompareFwdConv2D(input_shape, filter_shape, conv_strides, padding)
