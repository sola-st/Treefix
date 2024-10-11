# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
self._testSpecialCasesVariable()
for dtype in _TEST_DTYPES:
    self._testHugeNumberOfTensorsVariable(dtype)
