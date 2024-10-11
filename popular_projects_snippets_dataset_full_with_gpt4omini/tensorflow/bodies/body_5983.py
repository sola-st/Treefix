# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
def dataset_fn(input_context):
    batch_size = input_context.get_per_replica_batch_size(24)
    dataset = dataset_ops.DatasetV2.from_tensors(
        constant_op.constant([0, 1, 3], dtype=dtypes.int64))
    dataset = dataset.repeat().batch(batch_size, drop_remainder=True)
    dataset = dataset.shard(input_context.num_input_pipelines,
                            input_context.input_pipeline_id)
    dataset = dataset.prefetch(2)  # This prefetches 2 batches per device.
    dataset = dataset.map(lookup_table.lookup)
    exit(dataset)
exit(strategy.distribute_datasets_from_function(dataset_fn))
