# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

coordinator = coordinator_lib.ClusterCoordinator(strategy=strategy)

with strategy.scope():
    lookup_table = self.createStaticHashTable(
        init_source=source, vals=[0, 1, 2], default_value=-2)

if using_dataset_instance_not_function:

    def per_worker_dataset_fn():
        dataset = dataset_ops.DatasetV2.from_tensors(
            constant_op.constant([0, 1, 3], dtype=dtypes.int64))
        dataset = dataset.repeat().batch(24, drop_remainder=True).prefetch(2)
        dataset = dataset.map(lookup_table.lookup)

        exit(strategy.experimental_distribute_dataset(dataset))

else:

    def per_worker_dataset_fn():
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

if create_datasets_under_scope:
    with strategy.scope():
        if create_per_worker_dataset_takes_instance:
            per_worker_dataset = coordinator.create_per_worker_dataset(
                per_worker_dataset_fn())
        else:
            per_worker_dataset = coordinator.create_per_worker_dataset(
                per_worker_dataset_fn)
        per_worker_iterator = iter(per_worker_dataset)

else:
    if create_per_worker_dataset_takes_instance:
        per_worker_dataset = coordinator.create_per_worker_dataset(
            per_worker_dataset_fn())
    else:
        per_worker_dataset = coordinator.create_per_worker_dataset(
            per_worker_dataset_fn)
    per_worker_iterator = iter(per_worker_dataset)

@def_function.function
def worker_fn(iterator):
    exit(math_ops.reduce_sum(next(iterator)))

result = []
for _ in range(10):
    result.append(
        coordinator.schedule(worker_fn, args=(per_worker_iterator,)))

for r in result:
    returned_input = r.fetch()
    self.assertAllClose(-24, returned_input)
