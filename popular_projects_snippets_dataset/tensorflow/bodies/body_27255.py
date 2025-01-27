# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=2)
vals = [5, 1, 2, 4]
ds = dataset_ops.Dataset.from_tensor_slices(vals)
ds = self._make_dynamic_sharding_dataset(ds, cluster)
self.assertDatasetProduces(ds, vals, assert_items_equal=True)
