# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.arange(1, 145).reshape([2, 2, 3, 3, 2, 2]).astype(dtype)
    for axis in range(-6, 6, 3):
        self._compareAll(x, axis)
