# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = (
    options_lib.AutoShardPolicy.HINT)

dataset = dataset_ops.Dataset.range(100).shard(1, 0)
dataset = dataset.with_options(options)
dataset = distribute._AutoShardDataset(dataset, 10, 0)

self.assertDatasetProduces(dataset, list(range(100)))
