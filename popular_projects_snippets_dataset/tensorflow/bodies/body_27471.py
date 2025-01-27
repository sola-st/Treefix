# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = (
    options_lib.AutoShardPolicy.OFF)

dataset = core_readers._TFRecordDataset(self._filenames)
dataset = dataset.with_options(options)
dataset = distribute._AutoShardDataset(dataset, 5, 0)

# Should return every record in every file since autosharding is turned off.
expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in range(0, 10)
    for r in range(0, 10)
]
self.assertDatasetProduces(dataset, expected)
