# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
nested_row_splits = [
    constant_op.constant([0, 2, 3, 3, 5], dtypes.int64),
    constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
]
nested_value_rowids = [
    constant_op.constant([0, 0, 1, 3, 3], dtypes.int64),
    constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
]
rt1 = RaggedTensor.from_nested_row_splits(values, nested_row_splits)
rt2 = RaggedTensor.from_nested_value_rowids(values, nested_value_rowids)

for rt in [rt1, rt2]:
    self.assertAllEqual(
        rt, [[[b'a', b'b'], []], [[b'c', b'd', b'e']], [], [[b'f'], [b'g']]])
    self.assertAllEqual(
        rt.values, [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g']])
    self.assertEqual(rt.values.shape.dims[0].value, 5)
    self.assertAllEqual(rt.value_rowids(), [0, 0, 1, 3, 3])
    self.assertAllEqual(rt.nrows(), 4)
    self.assertAllEqual(rt.row_splits, [0, 2, 3, 3, 5])
    self.assertAllEqual(rt.row_starts(), [0, 2, 3, 3])
    self.assertAllEqual(rt.row_limits(), [2, 3, 3, 5])
    self.assertAllEqual(rt.row_lengths(), [2, 1, 0, 2])
    self.assertAllEqual(rt.flat_values,
                        [b'a', b'b', b'c', b'd', b'e', b'f', b'g'])
    self.assertLen(rt.nested_row_splits, 2)
    self.assertAllEqual(rt.nested_row_splits[0], [0, 2, 3, 3, 5])
    self.assertAllEqual(rt.nested_row_splits[1], [0, 2, 2, 5, 6, 7])
    self.assertLen(rt.nested_value_rowids(), 2)
    self.assertAllEqual(rt.nested_value_rowids()[0], [0, 0, 1, 3, 3])
    self.assertAllEqual(rt.nested_value_rowids()[1], [0, 0, 2, 2, 2, 3, 4])
