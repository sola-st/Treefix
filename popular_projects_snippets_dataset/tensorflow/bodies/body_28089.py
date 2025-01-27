# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
ds = dataset_ops.Dataset.range(10).ignore_errors()
self.assertEqual(self.evaluate(ds.cardinality()), dataset_ops.UNKNOWN)
