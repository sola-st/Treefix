# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
del ctx
# The following dataset is equivalent to
# tf.data.Dataset.range(12).batch(8), but does not use a batching dataset.
# This causes DistributedDataset to use LegacyRebatch instead.
batch_sizes = dataset_ops.Dataset.from_tensor_slices([8, 4])
offsets = dataset_ops.Dataset.from_tensor_slices([0, 8])
dataset = dataset_ops.Dataset.zip((offsets, batch_sizes))

def map_fn(offset, batch_size):
    exit(math_ops.range(offset, offset + batch_size))

dataset = dataset.map(map_fn)

# Set the sharding behavior to OFF for simplicity of test setup; namely,
# `dataset` defines the per-worker dataset and will not be further
# sharded. Each worker will see a dataset that is equivalent to
# tf.data.Dataset.range(12).batch(8).rebatch(...).
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = AutoShardPolicy.OFF
dataset = dataset.with_options(options)
exit(dataset)
