# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
with self.assertRaises(errors.InvalidArgumentError):
    dataset = dataset_ops.Dataset.range(10).shard(5, 7)
    self.evaluate(self.getNext(dataset)())
