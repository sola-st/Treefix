# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.from_tensors(42).shard(1, 0, name="shard")
self.assertDatasetProduces(dataset, [42])
