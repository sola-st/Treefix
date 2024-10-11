# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset = dataset_ops.Dataset.range(20)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    data_transfer_protocol=self._get_data_transfer_protocol(),
    processing_mode=data_service_ops.ShardingPolicy.OFF)
self.assertDatasetProduces(dataset, list(range(20)))
