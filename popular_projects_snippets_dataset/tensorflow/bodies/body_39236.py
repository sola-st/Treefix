# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session() as sess:
    # concat(A, B, C):
    # [    1              ]
    # [2       1       1  ]
    # [3   4 2     1 0 2  ]
    sp_a = self._SparseTensor_3x3()
    sp_b = self._SparseTensor_3x5()
    sp_c = self._SparseTensor_3x2()

    for concat_dim in (-1, 1):
        sp_concat = sparse_ops.sparse_concat(concat_dim, [sp_a, sp_b, sp_c])

        self.assertEqual(sp_concat.indices.get_shape(), [10, 2])
        self.assertEqual(sp_concat.values.get_shape(), [10])
        self.assertEqual(sp_concat.dense_shape.get_shape(), [2])

        concat_out = self.evaluate(sp_concat)

        self.assertAllEqual(concat_out.indices, [[0, 2], [1, 0], [1, 4], [1, 8],
                                                 [2, 0], [2, 2], [2, 3], [2, 6],
                                                 [2, 7], [2, 8]])
        self.assertAllEqual(concat_out.values, [1, 2, 1, 1, 3, 4, 2, 1, 0, 2])
        self.assertAllEqual(concat_out.dense_shape, [3, 10])
