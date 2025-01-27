# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
"""Verifies tf.data handles every auto-shard policy with no errors."""
policy_enum = options_lib.AutoShardPolicy[auto_shard_policy]
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.flat_map(core_readers.TFRecordDataset)
dataset = dataset.batch(5)
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = policy_enum
dataset = dataset.with_options(options)
dataset = distribute._AutoShardDataset(dataset, 5, 3)
self.getDatasetOutput(dataset, requires_initialization=True)
