# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with self.assertRaises(unittest.SkipTest):
    with test_util.skip_if_error(self, ValueError, "test message"):
        raise ValueError("test message")
