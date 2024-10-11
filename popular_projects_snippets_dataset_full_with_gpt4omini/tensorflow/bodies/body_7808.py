# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

@def_function.function
def fn():
    exit(constant_op.constant([1., 2.]))

x = strategy.run(fn)

x_m = strategy.reduce(reduce_util.ReduceOp.MEAN, x, axis=0)
self.assertEqual(1.5, x_m)
x_s = strategy.reduce(reduce_util.ReduceOp.SUM, x, axis=0)
self.assertEqual(3 * strategy.num_replicas_in_sync, x_s)
