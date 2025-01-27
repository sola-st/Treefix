# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
for dtype in _TEST_DTYPES:
    inp = self._makeData((4, 4), dtype)
    self._compare(inp, 0, 4)
