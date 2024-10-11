# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset1 = dataset_ops.Dataset.range(10)
dataset2 = dataset_ops.Dataset.from_tensor_slices(list("Test dataset."))

with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Datasets with the same ID should have the same structure"):
    dataset_id1 = data_service_ops.register_dataset(
        cluster.dispatcher.target,
        dataset1,
        compression=None,
        dataset_id="dataset_id")
    dataset_id2 = data_service_ops.register_dataset(
        cluster.dispatcher.target,
        dataset2,
        compression=None,
        dataset_id="dataset_id")
    dataset1 = data_service_ops.from_dataset_id(
        dataset_id=dataset_id1,
        element_spec=dataset1.element_spec,
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        data_transfer_protocol=self._get_data_transfer_protocol(),
        service=cluster.dispatcher.target)
    dataset2 = data_service_ops.from_dataset_id(
        dataset_id=dataset_id2,
        element_spec=dataset2.element_spec,
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        data_transfer_protocol=self._get_data_transfer_protocol(),
        service=cluster.dispatcher.target)
    self.getDatasetOutput(dataset1)
    self.getDatasetOutput(dataset2)
