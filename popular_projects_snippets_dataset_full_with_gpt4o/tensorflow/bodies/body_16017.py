# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
x = x()
actual = x.offsets_in_rows()
self.assertAllEqual(expected, actual)
