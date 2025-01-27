# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_value_rowids([])
rp_nrows = rp.nrows()
self.assertEqual(rp.dtype, dtypes.int64)
self.assertEqual(rp.value_rowids().shape.as_list(), [0])
self.assertAllEqual(rp_nrows, 0)
