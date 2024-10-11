# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
# When deployment mode is unspecified, the client will read from any worker.
cluster = _make_service_cluster(
    num_workers=5, local_shard_index=1, deployment_mode=None)
dataset = dataset_ops.Dataset.range(20)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    processing_mode=data_service_ops.ShardingPolicy.FILE_OR_DATA)
self.assertDatasetProduces(
    dataset, list(range(20)), assert_items_equal=True)
