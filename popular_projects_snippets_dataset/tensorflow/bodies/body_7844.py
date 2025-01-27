# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
reduced = strategy.reduce(
    reduce_util.ReduceOp.SUM, array_ops.identity(1.), axis=None)
self.assertEqual(reduced.numpy(), 2.)
