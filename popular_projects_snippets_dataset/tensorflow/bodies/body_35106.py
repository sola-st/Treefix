# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
self.assertFalse(du.gen_new_seed(0, "salt") is None)
self.assertTrue(du.gen_new_seed(None, "salt") is None)
