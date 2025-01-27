# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
for dtype in [dtypes.int64, dtypes.int32]:
    self._compare([2, 4, 3, 2], [2, 2], [[0, 0], [0, 0]], dtype)
