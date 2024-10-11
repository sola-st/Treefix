# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
num_dims = 3
truth = ["{:03b}".format(i) for i in range(2**num_dims)]
output_array = _input_array(num_dims).reshape([-1])
self.assertAllEqualUnicode(truth, output_array)
