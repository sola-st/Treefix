# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.range(1024)
dataset = distribute._AutoShardDataset(dataset, 2, 0)
self.assertDatasetProduces(dataset, [i for i in range(1024) if i % 2 == 0])
