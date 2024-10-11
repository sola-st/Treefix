# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with self.assertRaisesRegex(ValueError, r"Can't compare dict to non-dict"):
    self.assertAllClose(1, {"a": 1})
with self.assertRaisesRegex(ValueError, r"Can't compare dict to non-dict"):
    self.assertAllClose({"a": 1}, 1)
