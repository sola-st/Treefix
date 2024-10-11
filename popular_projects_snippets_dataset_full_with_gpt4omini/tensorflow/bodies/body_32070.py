# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
input_array = [["this", "is", "a", "test"],
               ["please", "do", "not", "panic"]]
truth_dim_zero = ["thisplease", "isdo", "anot", "testpanic"]
truth_shape_dim_zero = [4]
truth_dim_one = ["thisisatest", "pleasedonotpanic"]
truth_shape_dim_one = [2]
self._testReduceJoin(
    input_array, truth_dim_zero, truth_shape_dim_zero, axis=0)
self._testReduceJoin(
    input_array, truth_dim_one, truth_shape_dim_one, axis=1)

expected_val = "thisisatestpleasedonotpanic"
expected_shape = []
self._testReduceJoin(input_array, expected_val, expected_shape, axis=None)

# Using axis=[] is a no-op.
expected_val = input_array
expected_shape = [2, 4]
self._testReduceJoin(input_array, expected_val, expected_shape, axis=[])
