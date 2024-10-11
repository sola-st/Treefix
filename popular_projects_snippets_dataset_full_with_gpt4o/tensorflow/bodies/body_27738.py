# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
ds1 = dataset_ops.Dataset.from_tensors([1.0]).repeat()
ds2 = dataset_ops.Dataset.from_tensors([2.0]).repeat()
ds = dataset_ops.Dataset.sample_from_datasets([ds1, ds2])
self.assertEqual(self.evaluate(ds.cardinality()), dataset_ops.INFINITE)
