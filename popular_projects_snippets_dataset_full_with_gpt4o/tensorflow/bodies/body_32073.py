# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
input_arrays = [
    _input_array(num_dims=5).reshape([2] * i + [1] + [2] * (5 - i))
    for i in range(6)
]
truth = _input_array(num_dims=5)
truth_shape = [2] * 5
for i in range(6):
    self._testReduceJoin(input_arrays[i], truth, truth_shape, axis=i)
