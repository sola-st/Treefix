# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_uniform_row_length(3, nrows=4)
self.assertAllEqual(4, rp.nrows())
self.assertAllEqual(3, rp.uniform_row_length())
self.assertAllEqual(12, rp.static_nvals)
