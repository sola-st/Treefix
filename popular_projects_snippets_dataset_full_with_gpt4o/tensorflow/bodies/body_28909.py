# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset_a = dataset_ops.Dataset.range(10)
dataset_b = dataset_ops.Dataset.range(10, 0, -1)
dataset = dataset_ops.Dataset.zip((dataset_a, dataset_b)).shard(5, 2)
self.assertDatasetProduces(dataset, expected_output=[(2, 8), (7, 3)])
