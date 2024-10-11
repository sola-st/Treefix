# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
"""Makes sure shards from all workers form the complete dataset."""
cluster = _make_service_cluster(num_workers=1, local_shard_index=0)
dataset = dataset_ops.Dataset.range(20)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    processing_mode=data_service_ops.ShardingPolicy.FILE_OR_DATA)
self.assertDatasetProduces(dataset, list(range(20)))
