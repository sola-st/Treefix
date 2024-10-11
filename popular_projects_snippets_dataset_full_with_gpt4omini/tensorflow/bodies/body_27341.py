# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset = dataset_ops.Dataset.range(10)
_ = data_service_ops.register_dataset(
    cluster.dispatcher.target,
    dataset,
    dataset_id="dataset_id",
    compression=self._get_compression())
dataset = data_service_ops.from_dataset_id(
    dataset_id="dataset_id",
    element_spec=dataset.element_spec,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    data_transfer_protocol=self._get_data_transfer_protocol(),
    service=cluster.dispatcher.target)
self.assertDatasetProduces(dataset, list(range(10)))
