# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
spec = RowPartitionSpec()
spec_b = copy.deepcopy(spec)
self.assertEqual(repr(spec), repr(spec_b))
