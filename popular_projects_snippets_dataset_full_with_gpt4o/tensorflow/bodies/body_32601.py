# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
self.assertFalse(self.evaluate(check_ops.is_non_decreasing([3, 2, 1])))
