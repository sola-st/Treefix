# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
num_dims = 3
truth_dim_zero = [["000100", "001101"], ["010110", "011111"]]
truth_dim_one = [["000010", "001011"], ["100110", "101111"]]
truth_dim_two = [["000001", "010011"], ["100101", "110111"]]
output_array_dim_zero = _joined_array(num_dims, reduce_dim=0)
output_array_dim_one = _joined_array(num_dims, reduce_dim=1)
output_array_dim_two = _joined_array(num_dims, reduce_dim=2)
self.assertAllEqualUnicode(truth_dim_zero, output_array_dim_zero)
self.assertAllEqualUnicode(truth_dim_one, output_array_dim_one)
self.assertAllEqualUnicode(truth_dim_two, output_array_dim_two)
