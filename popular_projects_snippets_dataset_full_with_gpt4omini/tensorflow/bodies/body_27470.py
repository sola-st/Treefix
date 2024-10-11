# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = (
    options_lib.AutoShardPolicy.DATA)

dataset = core_readers._TFRecordDataset(self._filenames)
dataset = dataset.with_options(options)
dataset = distribute._AutoShardDataset(dataset, 5, 0)

# Should return "Record (0,5) of file (0 --> 9)" since we are sharding by
# individual elements, we should be able to get some data from all files.
expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in range(0, 10)
    for r in (0, 5)
]
self.assertDatasetProduces(dataset, expected)
