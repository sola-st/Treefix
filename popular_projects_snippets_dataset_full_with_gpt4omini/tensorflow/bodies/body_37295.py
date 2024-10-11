# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.ones([1000000], dtype=dtype) / 1024
    self._compareAll(x, 0)
