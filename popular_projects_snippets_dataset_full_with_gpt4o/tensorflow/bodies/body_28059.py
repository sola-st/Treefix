# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

ds = dataset_ops.Dataset.range(10).map(
    lambda x: dataset_ops.Dataset.range(1))

with self.assertRaisesRegex(
    TypeError, r'`padded_batch` is not supported for datasets of datasets'):
    _ = ds.padded_batch(3)
