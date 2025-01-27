# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
input_array = _input_array(num_dims=5)
truths = [_joined_array(num_dims=5, reduce_dim=i) for i in range(5)]
truth_shape = [2] * 4
for i in range(5):
    self._testReduceJoin(input_array, truths[i], truth_shape, axis=i - 5)
