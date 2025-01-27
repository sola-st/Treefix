# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.range(1).shard(5, 2)
self.assertDatasetProduces(dataset, expected_output=[])
