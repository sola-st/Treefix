# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = lookup_ops.IdTableWithHashBuckets(None, num_oov_buckets=1)
self.assertIsNone(table.resource_handle)
