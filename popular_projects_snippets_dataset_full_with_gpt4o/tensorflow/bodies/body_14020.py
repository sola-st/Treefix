# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
rt = ragged_tensor.RaggedTensor.from_value_rowids(
    array_ops.constant([[1, 2], [3, 4], [5, 6]]), [0, 0, 1])
pst = _PrivateSpecialType(rt)
pst_shape = array_ops.shape_v2(pst)
st = structured_tensor.StructuredTensor.from_fields_and_rank({"r": pst}, 1)
st_shape = st._ragged_shape
self.assertEqual(1, st.rank)
self.assertAllEqual(pst_shape[0], st_shape[0])
