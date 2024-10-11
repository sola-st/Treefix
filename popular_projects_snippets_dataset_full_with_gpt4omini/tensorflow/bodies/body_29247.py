# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
rt = ragged_factory_ops.constant([[1, 2], [], [3]])
rt_s = structure.type_spec_from_value(rt)
rt_after = structure.from_tensor_list(rt_s,
                                      structure.to_tensor_list(rt_s, rt))
self.assertEqual(rt_after.row_splits.shape.as_list(),
                 rt.row_splits.shape.as_list())
self.assertEqual(rt_after.values.shape.as_list(), [None])

st = sparse_tensor.SparseTensor(
    indices=[[3, 4]], values=[-1], dense_shape=[4, 5])
st_s = structure.type_spec_from_value(st)
st_after = structure.from_tensor_list(st_s,
                                      structure.to_tensor_list(st_s, st))
self.assertEqual(st_after.indices.shape.as_list(), [None, 2])
self.assertEqual(st_after.values.shape.as_list(), [None])
self.assertEqual(st_after.dense_shape.shape.as_list(),
                 st.dense_shape.shape.as_list())
