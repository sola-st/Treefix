# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=num_workers)
a = dataset_ops.Dataset.range(100)
b = dataset_ops.Dataset.range(100, 200)
ds = a.concatenate(b)
ds = self._make_dynamic_sharding_dataset(ds, cluster)

assert_items_equal = (num_workers > 1)
self.assertDatasetProduces(
    ds, list(range(200)), assert_items_equal=assert_items_equal)
