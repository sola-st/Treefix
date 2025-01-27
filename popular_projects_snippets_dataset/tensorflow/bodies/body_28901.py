# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
ds = dataset_ops.Dataset.range(10)
with self.assertRaises(RuntimeError):
    ds.as_numpy_iterator()
