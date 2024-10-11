# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([3, 5, 2], dtype=dtypes.int32)
values = array_ops.zeros([3, 5, 7])
shape = [4, 6, 7]
self.evaluate(self.scatter_nd(indices, values, shape))
