# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
row_splits = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
value_rowids = constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
rt1 = RaggedTensor.from_row_splits(values, row_splits)
rt2 = RaggedTensor.from_value_rowids(values, value_rowids)

for rt in [rt1, rt2]:
    self.assertAllEqual(
        rt, [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g']])
    self.assertAllEqual(rt.values, [b'a', b'b', b'c', b'd', b'e', b'f', b'g'])
    self.assertEqual(rt.values.shape.dims[0].value, 7)
    self.assertAllEqual(rt.value_rowids(), [0, 0, 2, 2, 2, 3, 4])
    self.assertAllEqual(rt.nrows(), 5)
    self.assertAllEqual(rt.row_splits, [0, 2, 2, 5, 6, 7])
    self.assertAllEqual(rt.row_starts(), [0, 2, 2, 5, 6])
    self.assertAllEqual(rt.row_limits(), [2, 2, 5, 6, 7])
    self.assertAllEqual(rt.row_lengths(), [2, 0, 3, 1, 1])
    self.assertAllEqual(rt.flat_values,
                        [b'a', b'b', b'c', b'd', b'e', b'f', b'g'])
    self.assertLen(rt.nested_row_splits, 1)
    self.assertAllEqual(rt.nested_row_splits[0], [0, 2, 2, 5, 6, 7])
