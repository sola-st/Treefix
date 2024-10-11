# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
# If this line is being called under strategy.scope(), it becomes a
# DistributedTable. Interestingly, after
# `experimental_distribute_dataset` serializes the dataset on chief and
# deserializes it on workers, `lookup_table` becomes a
# RestoredDistributedTable instead of a DistributedTable. And when it’s
# `resource_handle` is being accessed on the worker, it does not detect
# a DispatchContext, so it returns the restored resource handle,
# which is also the one on the local worker. The LookupTableFindV2 ops
# is on the local worker, too.
lookup_table = self.createStaticHashTable(
    init_source=source, vals=[0, 1, 2], default_value=-2)

if create_datasets_under_scope:
    self.assertIsInstance(lookup_table, ps_values.DistributedTable)

dataset = dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64))
dataset = dataset.repeat().batch(24, drop_remainder=True).prefetch(2)
dataset = dataset.map(lookup_table.lookup)

exit(strategy.experimental_distribute_dataset(dataset))
