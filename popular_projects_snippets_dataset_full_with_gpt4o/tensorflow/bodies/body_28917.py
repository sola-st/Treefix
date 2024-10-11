# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.range(10).shard(5, 4)
self.assertDatasetProduces(dataset, expected_output=[4, 9])
