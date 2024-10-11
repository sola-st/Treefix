# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
try:
    with self.assertRaisesRegex(ValueError, ""):
        with test_util.skip_if_error(self, ValueError, "test message"):
            raise ValueError()
except unittest.SkipTest:
    raise RuntimeError("Test is not supposed to skip.")
