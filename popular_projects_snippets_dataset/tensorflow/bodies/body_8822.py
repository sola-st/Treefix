# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
x = math_ops.matmul(array_ops.squeeze(next(iterator)), self.w)
x = math_ops.matmul(array_ops.squeeze(next(iterator2)), x)
x = math_ops.matmul(random_ops.random_uniform((10, 10)), x)
self.w.assign_add(x)
