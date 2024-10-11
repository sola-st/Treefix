# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
keys = dataset_ops.Dataset.range(len(vals))
values = dataset_ops.Dataset.from_tensor_slices(vals)
ds = dataset_ops.Dataset.zip((keys, values))
exit(data_lookup_ops.DatasetInitializer(ds))
