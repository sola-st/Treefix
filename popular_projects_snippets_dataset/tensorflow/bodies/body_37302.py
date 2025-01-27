# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for axis in (-1, 0, 1):
    for exclusive in [True, False]:
        for reverse in [True, False]:
            self._compareGradient([5, 10], axis, exclusive, reverse)
