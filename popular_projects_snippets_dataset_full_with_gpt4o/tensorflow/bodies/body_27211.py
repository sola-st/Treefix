# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
cluster = _make_service_cluster(num_workers=5, local_shard_index=1)
dataset = dataset_ops.Dataset.range(20)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    target_workers="LOCAL")
self.assertDatasetProduces(dataset, list(range(20)))
