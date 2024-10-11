# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
rt = ragged_factory_ops.constant(
    [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [], [[[9, 10], [11, 12]]]],
    ragged_rank=1)
st = self.evaluate(rt.to_sparse())
self.assertAllEqual(st.values, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
self.assertAllEqual(
    st.indices,
    [
        [0, 0, 0, 0],  # index for value=1
        [0, 0, 0, 1],  # index for value=2
        [0, 0, 1, 0],  # index for value=3
        [0, 0, 1, 1],  # index for value=4
        [0, 1, 0, 0],  # index for value=5
        [0, 1, 0, 1],  # index for value=6
        [0, 1, 1, 0],  # index for value=7
        [0, 1, 1, 1],  # index for value=8
        [2, 0, 0, 0],  # index for value=9
        [2, 0, 0, 1],  # index for value=10
        [2, 0, 1, 0],  # index for value=11
        [2, 0, 1, 1],  # index for value=12
    ])
self.assertAllEqual(st.dense_shape, [3, 2, 2, 2])
