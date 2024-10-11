# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([0], dtypes.int32)
updates = array_ops.zeros([0], dtypes.int32)
shape = constant_op.constant([0], dtypes.int32)
scatter = self.scatter_nd(indices, updates, shape)

with self.cached_session():
    self.assertEqual(self.evaluate(scatter).size, 0)
