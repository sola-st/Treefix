# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=2)
num_elements = 100
ds = dataset_ops.Dataset.range(num_elements)
ds = self.make_distributed_dataset(
    ds, cluster, processing_mode="distributed_epoch")
self.assertDatasetProduces(
    ds, list(range(num_elements)), assert_items_equal=True)
