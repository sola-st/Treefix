# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.range(0)
with self.assertRaises(errors.OutOfRangeError):
    dataset = distribute._AutoShardDataset(dataset, 10, 0)
    self.evaluate(self.getNext(dataset)())
