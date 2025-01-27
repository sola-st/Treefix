# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
# TODO(wxinyi): Warn the user of the inefficiency of this workflow (i.e.
# creating `StaticHashTable` inside a `@tf.function`-wrapped `dataset_fn` to
# be distributed with `distribute_datasets_from_function` and
# `create_per_worker_dataset`.
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

coordinator = coordinator_lib.ClusterCoordinator(strategy=strategy)

with strategy.scope():

    def dataset_fn(input_context):
        some_out_of_range_tensor = constant_op.constant(10, dtype=dtypes.int64)
        lookuptable = self.createStaticHashTable(
            init_source=source, vals=[0, 1, 2], default_value=-2)

        self.assertNotIsInstance(lookuptable, ps_values.DistributedTable)

        generation_tensor = lookuptable.lookup(some_out_of_range_tensor)
        dataset = self.makeDatasetFromTensorWithoutUsingResource(
            input_context, generation_tensor)
        exit(dataset)

    @def_function.function
    def per_worker_dataset_fn():
        exit(strategy.distribute_datasets_from_function(dataset_fn))

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
        self.assertAllClose(-48, returned_input)
