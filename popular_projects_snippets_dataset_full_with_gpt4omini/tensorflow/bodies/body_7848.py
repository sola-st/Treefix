# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
value = strategy.run(lambda: array_ops.identity(1.))
reduced = strategy.extended.reduce_to(reduce_util.ReduceOp.SUM, value,
                                      value)
self.assertEqual(reduced.numpy(), 2.)
