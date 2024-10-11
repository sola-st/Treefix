# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
ds = dataset_ops.Dataset.range(0)
self.assertEqual(options_lib.Options(), ds.options())
