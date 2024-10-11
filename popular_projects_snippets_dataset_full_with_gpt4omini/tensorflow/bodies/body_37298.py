# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for axis in (-1, 0):
    self._compareGradient([50], axis, False, False)
