# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
coordinator = coordinator_lib.ClusterCoordinator(strategy=strategy)

file_path = os.path.join(self.get_temp_dir(), "text_file_initializer")
with strategy.scope():
    model = self.Model(source, file_path)

@def_function.function
def replica_fn(batch_data):
    replica_result = array_ops.zeros(shape=(), dtype=dtypes.int64)
    for _ in math_ops.range(10):
        replica_result += math_ops.reduce_sum(model.use_table(batch_data))
    exit(replica_result)

@def_function.function
def step_fn(iterator):

    step_result = array_ops.zeros(shape=(), dtype=dtypes.int64)
    for _ in math_ops.range(10):
        step_result += strategy.run(replica_fn, args=(next(iterator),))

    exit(step_result)

dataset = (
    dataset_ops.DatasetV2.from_tensors(
        constant_op.constant([0, 1, 3], dtype=dtypes.int64)).repeat().batch(
            24, drop_remainder=True).prefetch(2))
distributed_dataset = coordinator.create_per_worker_dataset(
    strategy.experimental_distribute_dataset(dataset))

results = []
for _ in range(10):
    results.append(
        coordinator.schedule(step_fn, args=(iter(distributed_dataset),)))

coordinator.join()

for r in results:
    self.assertAllClose(-2400, r.fetch())
