# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.range(13).shard(23, 21)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 0))
