# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
ds = dataset_ops.Dataset.range(3)
self.assertEqual([0, 1, 2], list(ds.as_numpy_iterator()))
