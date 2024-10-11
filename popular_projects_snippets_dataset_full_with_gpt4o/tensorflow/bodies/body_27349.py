# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=2,
    fault_tolerant_mode=False,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset = dataset_ops.Dataset.range(10).batch(1000, drop_remainder=True)
dataset = self.make_distributed_dataset(
    dataset,
    cluster,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    data_transfer_protocol=self._get_data_transfer_protocol())
self.assertDatasetProduces(dataset, [])
