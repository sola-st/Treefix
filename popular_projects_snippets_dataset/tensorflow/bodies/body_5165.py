# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations_test.py
with distribution.scope():
    one_per_replica = distribution.run(lambda: constant_op.constant(1))
    num_replicas = distribution.reduce(
        reduce_util.ReduceOp.SUM, one_per_replica, axis=None)
    self.assertEqual(2, self.evaluate(num_replicas))
