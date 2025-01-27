# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
del ctx
dataset = dataset_ops.Dataset.range(8).batch(3)

# Set the sharding behavior to OFF for simplicity of test setup; namely,
# `dataset` defines the per-worker dataset and will not be further
# sharded. Each worker will see a dataset that is
# tf.data.Dataset.range(12).batch(8).rebatch(...).
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = auto_shard_policy
dataset = dataset.with_options(options)
exit(dataset)
