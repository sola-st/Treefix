# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# Same object: x gets returned as-is.
x = RowPartition.from_row_splits([0, 3, 8, 8])
self.assertIs(x._merge_precomputed_encodings(x), x)

# Same encoding tensor objects: x gets returned as-is.
y = RowPartition.from_row_splits(x.row_splits(), validate=False)
self.assertIs(x._merge_precomputed_encodings(y), x)
