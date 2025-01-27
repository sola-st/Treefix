# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
keys = dataset_ops.Dataset.range(100)
values = dataset_ops.Dataset.range(100).map(
    lambda x: string_ops.as_string(x * 2))
values = values.batch(4)
ds = dataset_ops.Dataset.zip((keys, values))
with self.assertRaises(ValueError):
    lookup_ops.DatasetInitializer(ds)
