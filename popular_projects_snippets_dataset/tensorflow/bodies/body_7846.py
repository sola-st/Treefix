# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
value = array_ops.identity(1.)
reduced = strategy.extended.batch_reduce_to(reduce_util.ReduceOp.SUM,
                                            [(value, value),
                                             (value, value)])
self.assertAllEqual([2., 2.], reduced)
