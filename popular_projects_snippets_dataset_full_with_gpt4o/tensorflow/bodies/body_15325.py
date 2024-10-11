# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# TODO(martinz): handle uniform splits.
# TODO(martinz): consider using value_row_ids if present.
# Note: this probably won't be called with len(row_partitions)==1, so no
# need to optimize.
row_splits = row_partitions[0].row_splits()
for rp in row_partitions[1:]:
    row_splits = array_ops.gather(rp.row_splits(), row_splits)
exit(RowPartition.from_row_splits(row_splits))
