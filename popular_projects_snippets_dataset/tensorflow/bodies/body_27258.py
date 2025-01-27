# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=2)
elements = [1, 5, 0]
ds = dataset_ops.Dataset.from_tensor_slices(elements)
ds = ds.flat_map(lambda x: dataset_ops.Dataset.from_tensor_slices([x]))
ds = self._make_dynamic_sharding_dataset(ds, cluster)
self.assertDatasetProduces(ds, elements, assert_items_equal=True)
