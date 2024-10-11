# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
sp_a = self._SparseTensor_NoNonZeros((2, 3, 4))
sp_b = self._SparseTensor_NoNonZeros((2, 7, 4))
sp_c = self._SparseTensor_NoNonZeros((2, 5, 4))

with self.session() as sess:
    concat_dim = 1
    sp_concat = sparse_ops.sparse_concat(concat_dim, [sp_a, sp_b, sp_c])

    self.assertEqual(sp_concat.indices.get_shape(), [0, 3])
    self.assertEqual(sp_concat.values.get_shape(), [0])
    self.assertEqual(sp_concat.dense_shape.get_shape(), [3])

    concat_out = self.evaluate(sp_concat)

    self.assertEqual(concat_out.indices.shape, (0, 3))
    self.assertEqual(concat_out.values.shape, (0,))
    self.assertAllEqual(concat_out.dense_shape, [2, 15, 4])
