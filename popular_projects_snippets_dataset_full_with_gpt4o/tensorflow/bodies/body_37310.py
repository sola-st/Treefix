# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.arange(1, 21).reshape([2, 2, 5]).astype(dtype)
    for axis in (-3, -2, -1, 0, 1, 2):
        self._compareAll(x, axis)
