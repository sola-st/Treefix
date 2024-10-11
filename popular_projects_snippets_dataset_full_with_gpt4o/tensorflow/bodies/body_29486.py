# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([100000, 1], dtypes.int32)
values = np.random.randn(100000)
shape = [1]
val = self.evaluate(self.scatter_nd(indices, values, shape))
for _ in range(5):
    val2 = self.evaluate(self.scatter_nd(indices, values, shape))
    self.assertAllEqual(val, val2)
