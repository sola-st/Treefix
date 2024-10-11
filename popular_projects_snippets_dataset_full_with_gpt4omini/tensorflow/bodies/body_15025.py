# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# From section: "Component Tensors"
rt = RaggedTensor.from_row_splits(
    values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8, 8])
self.assertAllEqual(rt, [[3, 1, 4, 1], [], [5, 9, 2], [6], []])
del rt

# From section: "Alternative Row-Partitioning Schemes"
values = [3, 1, 4, 1, 5, 9, 2, 6]
rt1 = RaggedTensor.from_row_splits(values, row_splits=[0, 4, 4, 7, 8, 8])
rt2 = RaggedTensor.from_row_lengths(values, row_lengths=[4, 0, 3, 1, 0])
rt3 = RaggedTensor.from_value_rowids(
    values, value_rowids=[0, 0, 0, 0, 2, 2, 2, 3], nrows=5)
rt4 = RaggedTensor.from_row_starts(values, row_starts=[0, 4, 4, 7, 8])
rt5 = RaggedTensor.from_row_limits(values, row_limits=[4, 4, 7, 8, 8])
for rt in (rt1, rt2, rt3, rt4, rt5):
    self.assertAllEqual(rt, [[3, 1, 4, 1], [], [5, 9, 2], [6], []])
del rt1, rt2, rt3, rt4, rt5

# From section: "Multiple Ragged Dimensions"
inner_rt = RaggedTensor.from_row_splits(
    values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8, 8])
outer_rt = RaggedTensor.from_row_splits(
    values=inner_rt, row_splits=[0, 3, 3, 5])
self.assertEqual(outer_rt.ragged_rank, 2)
self.assertAllEqual(outer_rt,
                    [[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]])
del inner_rt, outer_rt

# From section: "Multiple Ragged Dimensions"
rt = RaggedTensor.from_nested_row_splits(
    flat_values=[3, 1, 4, 1, 5, 9, 2, 6],
    nested_row_splits=([0, 3, 3, 5], [0, 4, 4, 7, 8, 8]))
self.assertAllEqual(rt, [[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]])
del rt

# From section: "Uniform Inner Dimensions"
rt = RaggedTensor.from_row_splits(
    values=array_ops.ones([5, 3]), row_splits=[0, 2, 5])
self.assertAllEqual(
    rt, [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]])
self.assertEqual(rt.shape.as_list(), [2, None, 3])
del rt
