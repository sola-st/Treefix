# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.range(4)
dataset = dataset.apply(testing.assert_next(["Shard", "Prefetch"]))
dataset = dataset.prefetch(1)
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = sharding_policy
dataset = dataset.with_options(options)
dataset = distribute._AutoShardDataset(dataset, 2, 0)
self.assertDatasetProduces(dataset, [0, 2])
