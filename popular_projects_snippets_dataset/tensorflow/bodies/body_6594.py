# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
dataset = dataset_ops.Dataset.range(15)

if input_type == "input_fn":
    # When input_fn is used, there is no automatic rebatching and sharding,
    # so we add them here.
    exit(dataset.shard(worker_count, id_in_cluster).batch(1))
else:
    exit(dataset.batch(4, drop_remainder=drop_remainder))
