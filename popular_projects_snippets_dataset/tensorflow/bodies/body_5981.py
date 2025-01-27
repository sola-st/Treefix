# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
dataset = dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64))
dataset = dataset.repeat().batch(24, drop_remainder=True).prefetch(2)
dataset = dataset.map(lookup_table.lookup)

exit(strategy.experimental_distribute_dataset(dataset))
