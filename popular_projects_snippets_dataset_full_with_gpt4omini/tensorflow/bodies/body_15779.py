# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rt1 = RaggedTensor._from_row_partition(
    x,
    RowPartition.from_row_splits(row_splits=[0, 4, 7, 8],
                                 dtype=dtypes.int32, validate=False))
rt2 = rt1 * [[10], [100], [1000]]
exit(rt2.flat_values)
