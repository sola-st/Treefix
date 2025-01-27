# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
ds1 = dataset_ops.Dataset.range(10)
ds2 = dataset_ops.Dataset.range(10)
ds = dataset_ops.Dataset.zip((ds1, ds2))
cloned_ds = input_ops._clone_dataset(ds)
self._assert_datasets_equal(ds, cloned_ds)
