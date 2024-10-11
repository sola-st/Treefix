# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset1 = dataset_ops.Dataset.range(10)
dataset2 = dataset_ops.Dataset.range(10)
dataset_id1 = data_service_ops.register_dataset(
    cluster.dispatcher.target,
    dataset1,
    dataset_id="dataset_id",
    compression=self._get_compression())
dataset_id2 = data_service_ops.register_dataset(
    cluster.dispatcher.target,
    dataset2,
    dataset_id=different_dataset_id,
    compression=self._get_compression())
dataset1 = data_service_ops.from_dataset_id(
    dataset_id=dataset_id1,
    element_spec=dataset1.element_spec,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    service=cluster.dispatcher.target,
    data_transfer_protocol=self._get_data_transfer_protocol(),
    job_name="job_name")
dataset2 = data_service_ops.from_dataset_id(
    dataset_id=dataset_id2,
    element_spec=dataset2.element_spec,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    service=cluster.dispatcher.target,
    data_transfer_protocol=self._get_data_transfer_protocol(),
    job_name="job_name")
# `dataset1` and `dataset2` are different datasets.
self.assertDatasetProduces(dataset1, list(range(10)))
self.assertDatasetProduces(dataset2, list(range(10)))
