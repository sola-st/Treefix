# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# From section: "Component Tensors"
rp = RowPartition.from_row_splits(row_splits=[0, 4, 4, 7, 8, 8])
self.assertAllEqual(rp.row_splits(), [0, 4, 4, 7, 8, 8])
del rp

# From section: "Alternative Row-Partitioning Schemes"
rt1 = RowPartition.from_row_splits(row_splits=[0, 4, 4, 7, 8, 8])
rt2 = RowPartition.from_row_lengths(row_lengths=[4, 0, 3, 1, 0])
rt3 = RowPartition.from_value_rowids(
    value_rowids=[0, 0, 0, 0, 2, 2, 2, 3], nrows=5)
rt4 = RowPartition.from_row_starts(row_starts=[0, 4, 4, 7, 8], nvals=8)
rt5 = RowPartition.from_row_limits(row_limits=[4, 4, 7, 8, 8])
for rp in (rt1, rt2, rt3, rt4, rt5):
    self.assertAllEqual(rp.row_splits(), [0, 4, 4, 7, 8, 8])
del rt1, rt2, rt3, rt4, rt5

# From section: "Multiple Ragged Dimensions"
inner_rt = RowPartition.from_row_splits(row_splits=[0, 4, 4, 7, 8, 8])
outer_rt = RowPartition.from_row_splits(row_splits=[0, 3, 3, 5])
del inner_rt, outer_rt
