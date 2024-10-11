# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
rt = ragged_factory_ops.constant([[1, 2], [3, 4, 5], [6], [], [7]])
st = rt.to_sparse()
self.assertEqual(st.indices.shape.as_list(), [7, 2])
self.assertEqual(st.values.shape.as_list(), [7])
self.assertEqual(st.dense_shape.shape.as_list(), [2])

rt = ragged_factory_ops.constant([[[1, 2]], [], [[3, 4]], []],
                                 ragged_rank=1)
st = rt.to_sparse()
self.assertEqual(st.indices.shape.as_list(), [4, 3])
self.assertEqual(st.values.shape.as_list(), [4])
self.assertEqual(st.dense_shape.shape.as_list(), [3])

rt = ragged_factory_ops.constant([[[1], [2, 3, 4, 5, 6, 7]], [[]]])
st = rt.to_sparse()
self.assertEqual(st.indices.shape.as_list(), [7, 3])
self.assertEqual(st.values.shape.as_list(), [7])
self.assertEqual(st.dense_shape.shape.as_list(), [3])
