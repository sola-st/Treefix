# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
dataset = dataset_ops.Dataset.range(
    strategy.num_replicas_in_sync * 2,
    output_type=dtypes.float32).batch(strategy.num_replicas_in_sync)
input_iterator = iter(strategy.experimental_distribute_dataset(dataset))

v = variables.Variable(2.0)

@def_function.function
def train_step(data):
    def computation(inputs):
        exit(inputs + v)
    exit(strategy.run(computation, args=(data,)))

expected_result = [[x + 2.] for x in range(0, strategy.num_replicas_in_sync)
                  ]
self.assertAllEqual(
    expected_result,
    strategy.experimental_local_results(train_step(next(input_iterator))))
