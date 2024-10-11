# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
"""Tests passing a dataset ID of Python string."""
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset = dataset_ops.Dataset.range(10)
dataset_id = data_service_ops.register_dataset(
    cluster.dispatcher.target, dataset, compression=self._get_compression())
dataset_id_val = tensor_util.constant_value(dataset_id)
dataset_id_str = (
    dataset_id_val.decode()
    if isinstance(dataset_id_val, bytes) else str(dataset_id_val))
dataset = data_service_ops.from_dataset_id(
    dataset_id=dataset_id_str,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    data_transfer_protocol=self._get_data_transfer_protocol(),
    service=cluster.dispatcher.target,
    job_name="job_name")
self.assertDatasetProduces(dataset, list(range(10)))
