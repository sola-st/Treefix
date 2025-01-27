# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_device_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 10
with ops.device(self._devices[0]):
    dataset = dataset_ops.Dataset.range(num_elements)
    element_spec = dataset.element_spec
    dataset_id = data_service_ops.register_dataset(
        cluster.dispatcher_address(), dataset)
    dataset = data_service_ops.from_dataset_id(
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        service=cluster.dispatcher_address(),
        dataset_id=dataset_id,
        element_spec=element_spec)
    self.assertDatasetProduces(dataset, list(range(num_elements)))

with ops.device(self._devices[1]):
    dataset = data_service_ops.from_dataset_id(
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        service=cluster.dispatcher_address(),
        dataset_id=dataset_id,
        element_spec=dataset.element_spec)
    self.assertDatasetProduces(dataset, list(range(num_elements)))
