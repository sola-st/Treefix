# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/testdata/generate_checkpoint.py
default_value = -1
empty_key = 0
deleted_key = -1
self.lookup_table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=default_value,
    empty_key=empty_key,
    deleted_key=deleted_key,
    name="t1",
    initial_num_buckets=32)
self.lookup_table.insert(1, 1)
self.lookup_table.insert(2, 4)
