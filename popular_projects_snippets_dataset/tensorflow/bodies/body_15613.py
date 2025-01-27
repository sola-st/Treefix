# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
rt = ragged_factory_ops.constant([[1, 2, 3], [4], [], [5, 6]])
st = self.evaluate(rt.to_sparse())
self.assertAllEqual(st.indices,
                    [[0, 0], [0, 1], [0, 2], [1, 0], [3, 0], [3, 1]])
self.assertAllEqual(st.values, [1, 2, 3, 4, 5, 6])
self.assertAllEqual(st.dense_shape, [4, 3])
