# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = rp()
expected = expected()
actual = rp._merge_with_spec(spec)
self.assertAllEqual(actual.row_splits(), expected.row_splits())
self.assertAllEqual(actual.static_nrows, expected.static_nrows)
self.assertAllEqual(actual.static_nvals, expected.static_nvals)
