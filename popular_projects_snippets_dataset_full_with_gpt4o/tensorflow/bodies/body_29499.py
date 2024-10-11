# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
a = array_ops.zeros([1])
indices = array_ops.zeros([100000, 1], dtypes.int32)
values = np.random.randn(100000)
val = self.evaluate(array_ops.tensor_scatter_update(a, indices, values))
for _ in range(5):
    val2 = self.evaluate(array_ops.tensor_scatter_update(a, indices, values))
    self.assertAllEqual(val, val2)
