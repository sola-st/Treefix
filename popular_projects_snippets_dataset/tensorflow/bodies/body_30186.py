# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
sp_value = sparse_tensor.SparseTensorValue(
    indices=((0, 1), (1, 0)), values=(42, 24), dense_shape=(2, 2))
self.assertAllEqual((2, 2), self.evaluate(array_ops.shape(sp_value)))
self.assertEqual(4, self.evaluate(array_ops.size(sp_value)))
self.assertEqual(2, self.evaluate(array_ops.rank(sp_value)))

sp = sparse_tensor.SparseTensor.from_value(sp_value)
self.assertAllEqual((2, 2), self.evaluate(array_ops.shape(sp)))
self.assertEqual(4, self.evaluate(array_ops.size(sp)))
self.assertEqual(2, self.evaluate(array_ops.rank(sp)))
