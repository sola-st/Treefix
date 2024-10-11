# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
self._testLargeInput([1])
self._testLargeInput([10])
self._testLargeInput([5, 10])
self._testLargeInput([50, 100])
self._testLargeInput([50, 10000])
self._testLargeInput([50, 10, 100])
self._testLargeInput([50, 10, 10, 100])
