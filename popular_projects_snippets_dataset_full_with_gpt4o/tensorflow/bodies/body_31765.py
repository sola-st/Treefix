# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
inputs = [[2.2, 4.4, 1.1], [5.5, 3.3, 6.6]]
self._validateNthElement(inputs, dtypes.float64, 2, False, [4.4, 6.6])
self._validateNthElement(inputs, dtypes.float64, 2, True, [1.1, 3.3])
