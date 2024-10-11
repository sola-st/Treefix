# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
num_elements = 10
cluster = data_service_test_base.TestCluster(num_workers=1)
a = dataset_ops.Dataset.range(num_elements)

ds = dataset_ops.Dataset.zip((a, a))
ds = dataset_ops.Dataset.zip((a, a, ds, a))
ds = self._make_dynamic_sharding_dataset(ds, cluster)

b = list(range(10))
self.assertDatasetProduces(ds, list(zip(b, b, zip(b, b), b)))
