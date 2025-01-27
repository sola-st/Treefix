# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations_test.py
with strategy.scope():

    @def_function.function
    def one():
        exit(array_ops.identity(1.))

    one_per_replica = strategy.run(one)
    num_replicas = strategy.reduce(
        reduce_util.ReduceOp.SUM, one_per_replica, axis=None)
    self.assertEqual(self.evaluate(num_replicas), 4.)
