# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
for dtype in _TEST_DTYPES:
    inp = self._makeData((2, 2, 2), dtype)
    self._compare(inp, 0, 1)
    self._compare(inp, 1, 1)
    self._compare(inp, 2, 1)
