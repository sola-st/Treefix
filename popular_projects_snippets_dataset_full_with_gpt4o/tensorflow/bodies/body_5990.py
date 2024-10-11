# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py

if using_dataset_instance_not_function and (
    not create_per_worker_dataset_takes_instance):
    # This is the case that uses the `experimental_distribute_dataset` API to
    # distribute dataset (instead of the `distribute_datasets_from_function`
    # API), and passes `create_per_worker_dataset` a function that returns
    # the distributed dataset (instead of passing it the distributed dataset
    # directly).
    # TODO(b/201775366): evaluate whether we need to handle this case
    self.skipTest("Failed to serialize the input pipeline graph")

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
coordinator = coordinator_lib.ClusterCoordinator(strategy=strategy)

if using_dataset_instance_not_function:

    def per_worker_dataset_fn():
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

else:

    def per_worker_dataset_fn():

        def dataset_fn(input_context):
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
