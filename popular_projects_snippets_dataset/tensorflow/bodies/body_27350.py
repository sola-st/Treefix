# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
num_workers = 2
cluster = data_service_test_base.TestCluster(
    num_workers=num_workers,
    fault_tolerant_mode=False,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset = dataset_ops.Dataset.range(10).batch(1000, drop_remainder=False)
dataset = self.make_distributed_dataset(
    dataset,
    cluster,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    data_transfer_protocol=self._get_data_transfer_protocol())
self.assertDatasetProduces(dataset, [list(range(10))] * num_workers)
