# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for axis in (-2, -1, 0, 1):
    for exclusive in [True, False]:
        for reverse in [True, False]:
            self._compareGradient([2, 4], axis, exclusive, reverse)
