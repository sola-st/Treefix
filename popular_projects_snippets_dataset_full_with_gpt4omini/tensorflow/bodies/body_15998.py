# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
a = RowPartition.from_uniform_row_length(
    nvals=0, uniform_row_length=0, nrows=10)
self.assertEqual(self.evaluate(a.nvals()), 0)
self.assertEqual(self.evaluate(a.nrows()), 10)
