# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
x = "hi"
self.assertIs(x, tensor_util.constant_value(x))
