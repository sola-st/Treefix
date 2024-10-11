# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([1, 2, 3], dtype=dtypes.int32)
values = array_ops.zeros([1, 2, 6, 7, 8, 9])
shape = [3, 4, 5, 6, 7, 8, 9]
self.evaluate(self.scatter_nd(indices, values, shape))
