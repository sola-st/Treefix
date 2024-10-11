# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session() as sess:
    # concat(A):
    # [    1]
    # [2    ]
    # [3   4]
    for sp_a in (self._SparseTensorValue_3x3(), self._SparseTensor_3x3()):
        # Note that we ignore concat_dim in this case since we short-circuit the
        # single-input case in python.
        for concat_dim in (-2000, 1, 2000):
            sp_concat = sparse_ops.sparse_concat(concat_dim, [sp_a])

            self.assertEqual(sp_concat.indices.get_shape(), [4, 2])
            self.assertEqual(sp_concat.values.get_shape(), [4])
            self.assertEqual(sp_concat.dense_shape.get_shape(), [2])

            concat_out = self.evaluate(sp_concat)

            self.assertAllEqual(concat_out.indices,
                                [[0, 2], [1, 0], [2, 0], [2, 2]])
            self.assertAllEqual(concat_out.values, [1, 2, 3, 4])
            self.assertAllEqual(concat_out.dense_shape, [3, 3])
