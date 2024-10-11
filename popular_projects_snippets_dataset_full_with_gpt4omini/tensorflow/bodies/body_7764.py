# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy()

inputs = strategy.make_input_fn_iterator(
    lambda _: dataset_ops.Dataset.from_tensor_slices([2., 3.]))

self.evaluate(inputs.initialize())
per_replica_outputs = strategy.run(
    def_function.function(math_ops.square), args=(next(inputs),))

with strategy.scope():
    mean = strategy.reduce(reduce_util.ReduceOp.MEAN, per_replica_outputs,
                           axis=None)
    self.assertEqual(6.5, self.evaluate(mean))
