# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=3)
a = dataset_ops.Dataset.range(50)
b = dataset_ops.Dataset.range(10).repeat(10)

ds = dataset_ops.Dataset.zip((a, b))
ds = self._make_dynamic_sharding_dataset(ds, cluster)

self.assertLen(self.getDatasetOutput(ds), 50)
