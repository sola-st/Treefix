# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
cluster = data_service_test_base.TestCluster(num_workers=2)
dataset = dataset_fn()
dataset = self.make_distributed_dataset(
    dataset, cluster=cluster, processing_mode=sharding_policy)
self.assertEqual(self.evaluate(dataset.cardinality()), expected_result)
