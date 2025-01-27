# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session() as sess:
    # concat(A, D):
    # [    1]
    # [2    ]
    # [3   4]
    # [  1  ]
    # [1   2]
    sp_a = self._SparseTensor_3x3()
    sp_d = self._SparseTensor_2x3()

    for concat_dim in (-2, 0):
        sp_concat = sparse_ops.sparse_concat(concat_dim, [sp_a, sp_d])

        self.assertEqual(sp_concat.indices.get_shape(), [7, 2])
        self.assertEqual(sp_concat.values.get_shape(), [7])
        self.assertEqual(sp_concat.dense_shape.get_shape(), [2])

        concat_out = self.evaluate(sp_concat)

        self.assertAllEqual(
            concat_out.indices,
            [[0, 2], [1, 0], [2, 0], [2, 2], [3, 1], [4, 0], [4, 2]])
        self.assertAllEqual(concat_out.values, np.array([1, 2, 3, 4, 1, 1, 2]))
        self.assertAllEqual(concat_out.dense_shape, np.array([5, 3]))
