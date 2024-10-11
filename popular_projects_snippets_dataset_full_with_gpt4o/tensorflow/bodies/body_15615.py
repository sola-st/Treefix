# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
rt = ragged_factory_ops.constant(
    [[[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]], [[11, 12]], [], [[13, 14]]
    ],
    ragged_rank=1)
st = self.evaluate(rt.to_sparse())
self.assertAllEqual(st.indices,
                    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0],
                     [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1],
                     [2, 0, 0], [2, 0, 1], [4, 0, 0], [4, 0, 1]])
self.assertAllEqual(st.values,
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
self.assertAllEqual(st.dense_shape, [5, 3, 2])
