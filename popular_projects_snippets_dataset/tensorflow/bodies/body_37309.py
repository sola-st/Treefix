# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.arange(1, 11).reshape([2, 5]).astype(dtype)
    for axis in (-2, -1, 0, 1):
        self._compareAll(x, axis)
