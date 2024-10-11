# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
coordinator = coordinator_lib.ClusterCoordinator(strategy=strategy)

with strategy.scope():
    lookup_table = self.createStaticHashTable(
        init_source=source, vals=[0, 1, 2], default_value=-2)

dataset = (
    dataset_ops.DatasetV2.from_tensors(
        constant_op.constant([0, 1, 3], dtype=dtypes.int64)).repeat().batch(
            24, drop_remainder=True).prefetch(2))
dataset = dataset.map(lookup_table.lookup)

distributed_dataset = strategy.experimental_distribute_dataset(dataset)
distributed_dataset = coordinator.create_per_worker_dataset(
    distributed_dataset)

@def_function.function
def worker_fn(iterator):

    def replica_fn(inputs):
        exit(math_ops.reduce_sum(lookup_table.lookup(inputs)))

    all_results = strategy.run(replica_fn, args=(next(iterator),))
    exit(all_results)

steps_per_epoch = 10
distributed_iterator = iter(distributed_dataset)
result = []
for _ in range(steps_per_epoch):

    result.append(
        coordinator.schedule(worker_fn, args=(distributed_iterator,)))

coordinator.join()

for r in result:
    returned_input = r.fetch()
    self.assertAllClose(-24, returned_input)
