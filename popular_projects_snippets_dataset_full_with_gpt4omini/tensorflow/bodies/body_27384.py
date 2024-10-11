# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    work_dir=data_service_test_base.NO_WORK_DIR,
    fault_tolerant_mode=False)
num_elements = 10
dataset = dataset_ops.Dataset.range(num_elements)
dataset_id = data_service_ops.register_dataset(cluster.dispatcher_address(),
                                               dataset)
with self.assertRaisesRegex(
    ValueError, "In graph mode `element_spec` must be provided manually."):
    _ = data_service_ops.from_dataset_id(
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        service=cluster.dispatcher_address(),
        dataset_id=dataset_id)
