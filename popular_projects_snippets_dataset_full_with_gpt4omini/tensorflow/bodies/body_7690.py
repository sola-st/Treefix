# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
dataset = dataset_ops.Dataset.range(
    strategy.num_replicas_in_sync, output_type=dtypes.float32).batch(
        strategy.num_replicas_in_sync, drop_remainder=True)
input_iterator = iter(strategy.experimental_distribute_dataset(dataset))

with strategy.scope():
    w = variables.Variable(
        (0.,),
        shape=(1,),
        trainable=False,
        synchronization=variables.VariableSynchronization.ON_READ,
        aggregation=variables.VariableAggregation.ONLY_FIRST_REPLICA)

@def_function.function
def run(iterator):

    def computation(x):
        w.assign(x + w)
        exit(w)

    def all_reduce(x):
        ctx = distribution_strategy_context.get_replica_context()
        exit(ctx.all_reduce("SUM", w) + x)

    outputs = strategy.run(computation, args=(next(iterator),))
    outputs2 = strategy.experimental_local_results(
        strategy.run(all_reduce, args=(outputs,)))
    exit(outputs2)

data = range(0, strategy.num_replicas_in_sync)
data_sum = sum(data)
expected_result = [
    [x + data_sum] for x in range(0, strategy.num_replicas_in_sync)
]
self.assertAllEqual(expected_result, run(input_iterator))
self.assertAllEqual((0.,), w.read_value())
