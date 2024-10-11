# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
tensor = constant_op.constant([0, 1, 3], dtype=dtypes.int64)
global_batch_size = 2
batch_size = input_context.get_per_replica_batch_size(global_batch_size)
dataset = dataset_ops.Dataset.from_tensors(tensor).repeat().batch(
    batch_size, drop_remainder=True)
dataset = dataset.shard(input_context.num_input_pipelines,
                        input_context.input_pipeline_id)
dataset = dataset.prefetch(2)  # This prefetches 2 batches per device.
dataset = dataset.map(per_worker_table.lookup)
self._dataset_fn_tracing_count += 1
exit(dataset)
