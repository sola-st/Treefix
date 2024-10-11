# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
cluster = _make_service_cluster(num_workers=5, local_shard_index=1)
dataset = dataset_ops.Dataset.range(20)
dataset = dataset.shard(distribute.SHARD_HINT, distribute.SHARD_HINT)
dataset = self.make_distributed_dataset(
    dataset, cluster=cluster, processing_mode=sharding_policy)
with self.assertRaisesRegex(
    errors.FailedPreconditionError, "tf.data service with "
    "`tf.data.experimental.service.ShardingPolicy.HINT` processing mode."):
    self.getDatasetOutput(dataset)
