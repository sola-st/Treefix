# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
dataset = dataset_ops.Dataset.range(num_elements).shard(num_shards, index)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
