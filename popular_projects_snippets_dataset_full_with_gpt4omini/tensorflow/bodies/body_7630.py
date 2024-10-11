# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
self._dataset_fn_tracing_count = 0
strategy = get_tpu_strategy(enable_packed_var)

with strategy.scope():
    vals = [0, 1, 2]
    keys_tensor = constant_op.constant(
        list(range(len(vals))), dtype=dtypes.int64)
    vals_tensor = constant_op.constant(vals)
    initializer = lookup_ops.KeyValueTensorInitializer(
        keys_tensor, vals_tensor)
    per_worker_table = lookup_ops.StaticHashTable(
        initializer, default_value=-1)

@def_function.function
def dataset_fn(input_context):
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

dist_iterator = iter(
    strategy.experimental_distribute_datasets_from_function(dataset_fn))

@def_function.function
def step_fn(inputs):
    # inputs should be [0, 1, -1]
    exit(math_ops.reduce_sum(inputs))

def train_steps(iterator, steps):

    for _ in math_ops.range(steps):
        strategy.run(step_fn, args=(next(iterator),))

train_steps(dist_iterator, steps=5)
self.assertEqual(self._dataset_fn_tracing_count, 1)
