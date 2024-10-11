# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
inputs = [2.2, 4.4, 1.1, 5.5, 3.3]
self._validateNthElement(inputs, dtypes.float32, 1, False, 2.2)
self._validateNthElement(inputs, dtypes.float32, 1, True, 4.4)
