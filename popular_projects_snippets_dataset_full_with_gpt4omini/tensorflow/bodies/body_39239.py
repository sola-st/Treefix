# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session(use_gpu=False) as sess:
    # concat(A, B):
    # [    a          ]
    # [b       e      ]
    # [c   d f     g h]
    sp_a = self._SparseTensor_String3x3()
    sp_b = self._SparseTensor_String3x5()

    for concat_dim in (-1, 1):
        sp_concat = sparse_ops.sparse_concat(concat_dim, [sp_a, sp_b])

        self.assertEqual(sp_concat.indices.get_shape(), [8, 2])
        self.assertEqual(sp_concat.values.get_shape(), [8])
        self.assertEqual(sp_concat.dense_shape.get_shape(), [2])

        concat_out = self.evaluate(sp_concat)

        self.assertAllEqual(
            concat_out.indices,
            [[0, 2], [1, 0], [1, 4], [2, 0], [2, 2], [2, 3], [2, 6], [2, 7]])
        self.assertAllEqual(concat_out.values,
                            [b"a", b"b", b"e", b"c", b"d", b"f", b"g", b"h"])
        self.assertAllEqual(concat_out.dense_shape, [3, 8])
