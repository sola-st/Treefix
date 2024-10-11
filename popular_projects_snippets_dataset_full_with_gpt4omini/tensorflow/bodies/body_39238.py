# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
sp_a = self._SparseTensor_NoNonZeros((2, 7, 4))
sp_b = self._SparseTensor_2x3x4()
sp_c = self._SparseTensor_NoNonZeros((2, 5, 4))
output_nnz = sp_b.indices.get_shape()[0]

with self.session() as sess:
    concat_dim = 1
    sp_concat = sparse_ops.sparse_concat(concat_dim, [sp_a, sp_b, sp_c])

    self.assertEqual(sp_concat.indices.get_shape(), [output_nnz, 3])
    self.assertEqual(sp_concat.values.get_shape(), [output_nnz])
    self.assertEqual(sp_concat.dense_shape.get_shape(), [3])

    concat_out = self.evaluate(sp_concat)

    self.assertAllEqual(concat_out.indices,
                        sp_b.indices + [0, sp_a.dense_shape[1], 0])
    self.assertAllEqual(concat_out.values, sp_b.values)
    self.assertAllEqual(concat_out.dense_shape, [2, 15, 4])
