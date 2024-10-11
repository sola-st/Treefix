# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_row_starts([0, 3, 6], nvals=12)
self.assertAllEqual(12, rp.static_nvals)
