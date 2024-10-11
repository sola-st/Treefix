# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
for dtype in _TEST_DTYPES:
    self._compare(self._makeData((6, 10, 18), dtype), 0, 3)
    self._compare(self._makeData((6, 7, 18), dtype), 0, 3)
    self._compare(self._makeData((6, 7, 9), dtype), 0, 3)
