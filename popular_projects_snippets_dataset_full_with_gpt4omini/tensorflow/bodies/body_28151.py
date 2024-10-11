# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py
for dtype in [dtypes.int32, dtypes.int64]:
    self._testSimpleHelper(dtype, [
        ([], []),
        ([1], [1]),
        ([1, 1, 1, 1, 1, 1, 1], [1]),
        ([1, 1, 1, 1, 0], [1, 0]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 2, 4, 3, 2, 1, 2, 3, 4], [1, 2, 4, 3]),
        ([[1], [1, 1], [1, 1, 1]], [[1], [1, 1], [1, 1, 1]]),
        ([[1, 1], [1, 1], [2, 2], [3, 3], [1, 1]], [[1, 1], [2, 2], [3, 3]]),
    ])
