# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
# Note: np.split returns a rank-0 empty ndarray
# if the input ndarray is empty.
for dtype in _TEST_DTYPES:
    inp = self._makeData((8, 0, 21), dtype)
    self._testEmpty(inp, 0, 2, (4, 0, 21))
    self._testEmpty(inp, 0, 4, (2, 0, 21))
    self._testEmpty(inp, 1, 4, (8, 0, 21))
    self._testEmpty(inp, 2, 3, (8, 0, 7))
    self._testEmpty(inp, 2, 7, (8, 0, 3))
