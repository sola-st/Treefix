# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for exclusive in [True, False]:
    for reverse in [True, False]:
        self._compare(x, axis, exclusive, reverse)
