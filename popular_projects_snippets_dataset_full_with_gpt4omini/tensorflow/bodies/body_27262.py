# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=2)
num_repeats = 5
num_elements = 20
ds = dataset_ops.Dataset.range(num_elements)
ds = self._make_dynamic_sharding_dataset(ds, cluster)
ds = ds.repeat(num_repeats)
self.assertDatasetProduces(
    ds, num_repeats * list(range(num_elements)), assert_items_equal=True)
