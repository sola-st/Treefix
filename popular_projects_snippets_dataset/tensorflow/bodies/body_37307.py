# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for dtype in (np.float16, np.float32, np.float64):
    for nan_idx in range(0, 5):
        x = np.arange(1, 6).reshape([5]).astype(dtype)
        x[nan_idx] = np.nan
        for axis in (-1, 0):
            self._compareAll(x, axis)
