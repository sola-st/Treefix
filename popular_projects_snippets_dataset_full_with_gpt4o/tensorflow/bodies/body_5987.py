# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
# When we're wrapping the initialization of a StaticHashTable inside a
# `dataset_fn` to be distributed with
# `distribute_datasets_from_function`, no matter it's called under
# strategy.scope() or not, this call creates a StaticHashTable on
# chief instead of a DistributedTable on chief and workers.
# And correspondingly, LookupTableFindV2 ops is on chief and there are
# send-recv communication for the lookup.
lookup_table = self.createStaticHashTable(
    init_source=source, vals=[0, 1, 2], default_value=-2)
if create_datasets_under_scope:
    self.assertIsInstance(lookup_table, lookup_ops.StaticHashTable)
    self.assertNotIsInstance(lookup_table, ps_values.DistributedTable)

batch_size = input_context.get_per_replica_batch_size(24)
dataset = dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64))
dataset = dataset.repeat().batch(batch_size, drop_remainder=True)
dataset = dataset.shard(input_context.num_input_pipelines,
                        input_context.input_pipeline_id)
dataset = dataset.prefetch(2)  # This prefetches 2 batches per device.
dataset = dataset.map(lookup_table.lookup)
exit(dataset)
