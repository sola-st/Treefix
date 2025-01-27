# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
nvals = 16
a1 = RowPartition.from_uniform_row_length(
    nvals=nvals, uniform_row_length=2)
self.assertAllEqual(a1.uniform_row_length(), 2)
self.assertAllEqual(a1.nrows(), 8)
