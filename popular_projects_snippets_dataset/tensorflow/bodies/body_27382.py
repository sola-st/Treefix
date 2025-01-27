# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
cluster = data_service_test_base.TestCluster(num_workers=2)
dataset = dataset_fn()
dataset_id = data_service_ops.register_dataset(
    cluster.dispatcher.target, dataset=dataset)
dataset = data_service_ops.from_dataset_id(
    processing_mode=sharding_policy,
    service=cluster.dispatcher.target,
    dataset_id=dataset_id,
    element_spec=dataset.element_spec)
self.assertEqual(self.evaluate(dataset.cardinality()), expected_result)
