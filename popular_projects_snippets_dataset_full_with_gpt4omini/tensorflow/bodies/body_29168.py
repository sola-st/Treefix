# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
st_0 = sparse_tensor.SparseTensorValue(
    indices=np.array([[0]]),
    values=np.array([0], dtype=np.int64),
    dense_shape=np.array([1]))
st_1 = sparse_tensor.SparseTensorValue(
    indices=np.array([[0, 0], [1, 1]]),
    values=np.array([-1., 1.], dtype=np.float32),
    dense_shape=np.array([2, 2]))
opt = optional_ops.Optional.from_value((st_0, st_1))
self.assertTrue(self.evaluate(opt.has_value()))
val_0, val_1 = opt.get_value()
for expected, actual in [(st_0, val_0), (st_1, val_1)]:
    self.assertAllEqual(expected.indices, self.evaluate(actual.indices))
    self.assertAllEqual(expected.values, self.evaluate(actual.values))
    self.assertAllEqual(expected.dense_shape,
                        self.evaluate(actual.dense_shape))
