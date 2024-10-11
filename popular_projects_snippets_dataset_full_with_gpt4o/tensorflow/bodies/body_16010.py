# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# The encoding tensors for `a` are a superset of the encoding tensors
# for `b`, and where they overlap, they the same tensor objects.
a = RowPartition.from_value_rowids([0, 0, 3, 4, 4, 4])
b = RowPartition.from_row_splits(a.row_splits(), validate=False)
self.assertIs(a._merge_precomputed_encodings(b), a)
self.assertIs(b._merge_precomputed_encodings(a), a)
self.assertIsNot(a, b)
