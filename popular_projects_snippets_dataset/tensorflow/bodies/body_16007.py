# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_row_splits([0, 2, 8])

rp_with_row_splits = rp._with_precomputed_row_splits()
self.assertTrue(rp_with_row_splits._has_precomputed_row_splits())

self.assertFalse(rp._has_precomputed_row_lengths())
rp_with_row_lengths = rp._with_precomputed_row_lengths()
self.assertTrue(rp_with_row_lengths._has_precomputed_row_lengths())

self.assertFalse(rp._has_precomputed_value_rowids())
rp_with_value_rowids = rp._with_precomputed_value_rowids()
self.assertTrue(rp_with_value_rowids._has_precomputed_value_rowids())

self.assertFalse(rp._has_precomputed_nrows())
rp_with_nrows = rp._with_precomputed_nrows()
self.assertTrue(rp_with_nrows._has_precomputed_nrows())

self.assertFalse(rp._has_precomputed_nvals())
rp_with_nvals = rp._with_precomputed_nvals()
self.assertTrue(rp_with_nvals._has_precomputed_nvals())
