# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options = options_lib.Options()
ds = dataset_ops.Dataset.range(0).with_options(options).cache()
self.assertEqual(options, ds.options())
