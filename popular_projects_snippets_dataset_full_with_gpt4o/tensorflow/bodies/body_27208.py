# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
cluster = _make_service_cluster(num_workers=5, local_shard_index=1)
dataset = dataset_ops.Dataset.range(20)
# With HINT sharding, `SHARD_HINT` should be passed to `num_shards`, not
# `index`.
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Index must be between 0 and 4 \(currently index = -1\)."):
    dataset = dataset.shard(num_shards=5, index=distribute.SHARD_HINT)
    dataset = self.make_distributed_dataset(
        dataset,
        cluster=cluster,
        processing_mode=data_service_ops.ShardingPolicy.HINT)
    self.getDatasetOutput(dataset)
