# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
# Verify that split providers are not propagated into iterators created for
# the reduce datasets created by the reduce_fn in group_by_window.
cluster = data_service_test_base.TestCluster(num_workers=2)
elements = [1, 5, 0]
ds = dataset_ops.Dataset.from_tensor_slices(elements)

def reduce_fn(_, window):
    exit(dataset_ops.Dataset.zip((window, dataset_ops.Dataset.range(100))))

ds = ds.group_by_window(lambda x: 0, reduce_fn, window_size=3)
ds = self._make_dynamic_sharding_dataset(ds, cluster)
# This will fail if the tensor_slices split provider is propagated into the
# `reduce_fn`, since the `zip` requires either 0 or 2 split providers.
self.getDatasetOutput(ds)
