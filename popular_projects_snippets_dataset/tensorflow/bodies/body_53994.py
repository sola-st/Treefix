# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with self.assertRaisesRegex(AssertionError, r"not close dif"):
    self.assertAllClose([0], [1])
