# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
value = strategy.run(lambda: array_ops.identity(1.))
reduced = strategy.reduce(reduce_util.ReduceOp.SUM, value, axis=None)
self.assertEqual(reduced.numpy(), 2.)
