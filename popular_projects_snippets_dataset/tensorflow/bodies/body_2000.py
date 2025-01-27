# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.zeros([0]).astype(dtype)
    for axis in (-1, 0):
        self._compareAll(x, axis)
