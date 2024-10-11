# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
self.assertAllClose(7, 7 + 1e-8)
with self.assertRaisesRegex(AssertionError, r"Not equal to tolerance"):
    self.assertAllClose(7, 7 + 1e-5)
