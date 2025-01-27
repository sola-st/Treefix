# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
self.assertFalse(self.evaluate(
    check_ops.is_strictly_increasing([1, 0, -1])))
