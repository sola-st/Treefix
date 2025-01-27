# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
x = 0
self.assertRaises(ValueError, decorator_utils.validate_callable, x, "test")
