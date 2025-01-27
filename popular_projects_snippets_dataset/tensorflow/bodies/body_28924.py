# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([]).shard(
    num_shards=2, index=1)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=0))
