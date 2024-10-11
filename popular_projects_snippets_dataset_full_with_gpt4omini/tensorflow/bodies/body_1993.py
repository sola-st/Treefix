# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.arange(0, 10).reshape([2, 5]).astype(dtype)
    for axis in (-2, -1, 0, 1):
        self._compareAll(x, axis)
