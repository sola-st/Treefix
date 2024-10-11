# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

@def_function.function
def input_fn():
    exit(dataset_ops.DatasetV2.range(1, 3))

with self.strategy.scope():
    v = variables.Variable(initial_value=1, dtype=dtypes.int64)

    def replica_fn(input_tensor):
        exit((input_tensor + v, input_tensor - v))

    @def_function.function
    def worker_fn(iterator):
        exit(self.strategy.run(replica_fn, args=(next(iterator),)))

per_worker_dataset = self.coordinator.create_per_worker_dataset(input_fn)

@contextlib.contextmanager
def _assert_logs_usage_warning():
    with self.assertLogs(level='WARNING') as logs:
        exit()

    self.assertIn(
        'A `tf.distribute.experimental.ParameterServerStrategy` method is '
        'invoked without using `ClusterCoordinator.schedule`. If you are not '
        'tracing a tf.function, this method is possibly executed on the '
        'coordinator, which can be slow. To properly dispatch functions to '
        'run on workers, methods like `run` or `reduce` should be used '
        'within a function passed to `tf.distribute.experimental.coordinator.'
        'ClusterCoordinator.schedule`.', logs.output[0])

with _assert_logs_usage_warning():
    # Invoking `run` without `coordinator.schedule` should result in a
    # warning.
    self.strategy.run(
        replica_fn, args=(constant_op.constant(1, dtype=dtypes.int64),))

# A proper `schedule` should succeed.
rv = self.coordinator.schedule(worker_fn, args=(iter(per_worker_dataset),))

with _assert_logs_usage_warning():
    # Invoking `run` without `coordinator.schedule` again should result in a
    # warning.
    self.strategy.run(
        replica_fn, args=(constant_op.constant(1, dtype=dtypes.int64),))

all_results = [(2, 0)] * self.strategy.num_replicas_in_sync
expected_result = []
for i in range(self.strategy.num_replicas_in_sync):
    expected_result.append(all_results[i])

self.assertAllEqual(
    tuple(expected_result),
    self.strategy.experimental_local_results(rv.fetch()))
