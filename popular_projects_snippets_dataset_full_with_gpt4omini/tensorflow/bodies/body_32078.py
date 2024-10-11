# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
num_dims = 3
input_array = _input_array(num_dims=num_dims)
# Also tests [].
for i in range(num_dims + 1):
    for permutation in itertools.permutations(range(num_dims), i):
        self._testMultipleReduceJoin(input_array, axis=permutation)
