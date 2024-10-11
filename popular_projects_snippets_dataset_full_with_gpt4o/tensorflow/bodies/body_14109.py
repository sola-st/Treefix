# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
if row_partitions is not None:
    row_partitions = [
        row_partition.RowPartition.from_row_splits(r) for r in row_partitions
    ]
st = StructuredTensor.from_fields({},
                                  shape=shape,
                                  row_partitions=row_partitions)
# NOTE: zeros_like is very robust. There aren't arguments that
# should cause this operation to fail.
actual = array_ops.zeros_like(st, dtype)
self.assertAllEqual(actual, expected)

actual2 = array_ops.zeros_like_v2(st, dtype)
self.assertAllEqual(actual2, expected)
