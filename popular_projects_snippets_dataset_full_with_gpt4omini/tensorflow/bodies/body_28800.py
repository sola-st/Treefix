# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
exit(self._counting_dataset(start, make_scan_fn(step)).take(take))
