# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
for dtype in [dtypes.int64, dtypes.int32]:
    self._compare([1, 2, 3, 5], [2, 2], [[0, 0], [0, 0]], dtype)
