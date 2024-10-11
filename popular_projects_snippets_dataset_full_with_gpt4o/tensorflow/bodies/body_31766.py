# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
inputs = [[[2, 4, 1], [5, -3, 6]],
          [[7, 9, -8], [9, 0, 4]]]
self._validateNthElement(inputs, dtypes.int32, 0, False,
                         [[1, -3], [-8, 0]])
self._validateNthElement(inputs, dtypes.int64, 0, True,
                         [[4, 6], [9, 9]])
