# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = rp()
actual = rp._merge_with_spec(spec)
self.assertAllEqual(actual.row_splits(), rp.row_splits())
self.assertAllEqual(actual.static_nrows, rp.static_nrows)
self.assertAllEqual(actual.static_nvals, rp.static_nvals)
