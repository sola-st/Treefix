# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session() as sess:
    sp_a = self._SparseTensor_3x3()
    sp_b = self._SparseTensor_3x5()
    sp_c = self._SparseTensor_3x2()
    sp_d = self._SparseTensor_2x3()
    for concat_dim0 in (-2, 0):
        for concat_dim1 in (-1, 1):
            sp_concat_dim0 = sparse_ops.sparse_concat(
                concat_dim0, [sp_a, sp_b, sp_c, sp_d], expand_nonconcat_dim=True)
            sp_concat_dim1 = sparse_ops.sparse_concat(
                concat_dim1, [sp_a, sp_b, sp_c, sp_d], expand_nonconcat_dim=True)

            sp_concat_dim0_out = self.evaluate(sp_concat_dim0)
            sp_concat_dim1_out = self.evaluate(sp_concat_dim1)

            self.assertAllEqual(sp_concat_dim0_out.indices,
                                [[0, 2], [1, 0], [2, 0], [2, 2], [4, 1], [5, 0],
                                 [5, 3], [5, 4], [7, 0], [8, 0], [9, 1], [10, 0],
                                 [10, 2]])
            self.assertAllEqual(sp_concat_dim0_out.values,
                                [1, 2, 3, 4, 1, 2, 1, 0, 1, 2, 1, 1, 2])
            self.assertAllEqual(sp_concat_dim0_out.dense_shape, [11, 5])

            self.assertAllEqual(sp_concat_dim1_out.indices,
                                [[0, 2], [0, 11], [1, 0], [1, 4], [1, 8], [1, 10],
                                 [1, 12], [2, 0], [2, 2], [2, 3], [2, 6], [2, 7],
                                 [2, 8]])
            self.assertAllEqual(sp_concat_dim1_out.values,
                                [1, 1, 2, 1, 1, 1, 2, 3, 4, 2, 1, 0, 2])
            self.assertAllEqual(sp_concat_dim1_out.dense_shape, [3, 13])
