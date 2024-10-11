# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
self.values = ops.convert_to_tensor(values)
self.mean = math_ops.reduce_mean(values)
self.max = math_ops.reduce_max(values)
