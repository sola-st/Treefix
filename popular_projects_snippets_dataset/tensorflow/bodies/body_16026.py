# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_uniform_row_length(3, nvals=12)
self.assertAllEqual(4, rp.static_nrows)
self.assertAllEqual(3, rp.static_uniform_row_length)
self.assertAllEqual(12, rp.static_nvals)
