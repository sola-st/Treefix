# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
v = variables.Variable([1, 2, 3])
self.assertTrue(tensor_util.is_tf_type(v))
