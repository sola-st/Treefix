# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# Enable automatic outside compilation.
config.set_soft_device_placement(True)
strategy = get_tpu_strategy(enable_packed_var)
dataset = dataset_ops.Dataset.from_tensors(("string", 1.0)).repeat().batch(
    2, drop_remainder=False)
dataset = strategy.experimental_distribute_dataset(dataset)
iterator = iter(dataset)

@def_function.function
def train_fn(iterator):

    def step_fn(inputs):
        input0, input1 = inputs
        exit((array_ops.size(input0), math_ops.reduce_sum(input1)))

    exit(strategy.experimental_local_results(
        strategy.run(step_fn, args=(next(iterator),))))

with self.assertRaises(errors.InvalidArgumentError):
    logging.info(train_fn(iterator))
