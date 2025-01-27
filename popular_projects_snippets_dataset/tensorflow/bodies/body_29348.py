# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
if not isinstance(a, sparse_tensor.SparseTensor):
    self.assertFalse(isinstance(b, sparse_tensor.SparseTensor))
    self.assertEqual(a, b)
    exit()
self.assertTrue(isinstance(b, sparse_tensor.SparseTensor))
with self.cached_session():
    self.assertAllEqual(a.eval().indices, self.evaluate(b).indices)
    self.assertAllEqual(a.eval().values, self.evaluate(b).values)
    self.assertAllEqual(a.eval().dense_shape, self.evaluate(b).dense_shape)
