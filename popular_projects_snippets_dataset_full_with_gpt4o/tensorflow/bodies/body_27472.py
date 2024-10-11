# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = (
    options_lib.AutoShardPolicy.FILE)

dataset = dataset_ops.Dataset.range(1024)
dataset = dataset.with_options(options)

# We are specifying that we want a file sharding policy, and this pipeline
# doesn't start with file reading, so we should error out.
with self.assertRaises(errors.NotFoundError):
    dataset = distribute._AutoShardDataset(dataset, 10, 0)
    self.evaluate(self.getNext(dataset)())
