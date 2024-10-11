# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
input_array = ["this", "is", "a", "test"]
truth = "thisisatest"
truth_shape = []
self._testReduceJoin(input_array, truth, truth_shape, axis=0)
