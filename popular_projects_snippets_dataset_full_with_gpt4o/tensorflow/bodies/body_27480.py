# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.list_files(self._filenames)
dataset = dataset.flat_map(core_readers.TFRecordDataset)
dataset = dataset.batch(5)

with self.assertRaises(errors.InvalidArgumentError):
    dataset = distribute._AutoShardDataset(dataset, 2, 2)
    self.evaluate(self.getNext(dataset)())
