# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
"""Returns a dataset made from `tensor`. To be called in a dataset_fn."""
global_batch_size = 24
batch_size = input_context.get_per_replica_batch_size(global_batch_size)
dataset = dataset_ops.DatasetV2.from_tensors(tensor).repeat().batch(
    batch_size, drop_remainder=True)
dataset = dataset.shard(input_context.num_input_pipelines,
                        input_context.input_pipeline_id)
dataset = dataset.prefetch(2)  # This prefetches 2 batches per device.
exit(dataset)
