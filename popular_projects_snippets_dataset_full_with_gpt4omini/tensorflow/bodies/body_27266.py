# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
num_elements = 10
cluster = data_service_test_base.TestCluster(num_workers=1)
a = dataset_ops.Dataset.range(num_elements)

ds = dataset_ops.Dataset.zip((a, a))
ds = self._make_dynamic_sharding_dataset(ds, cluster)

self.assertDatasetProduces(
    ds, list(zip(range(num_elements), range(num_elements))))
