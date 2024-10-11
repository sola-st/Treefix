# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
actual = a._merge_with(b)
actual_rev = b._merge_with(a)
self.assertEqual(actual, expected)
self.assertEqual(actual_rev, expected)
