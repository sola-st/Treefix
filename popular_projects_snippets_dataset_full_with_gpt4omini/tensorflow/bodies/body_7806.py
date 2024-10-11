# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
per_replica_value = strategy.experimental_distribute_values_from_function(
    lambda _: array_ops.ones((), dtypes.float32))

def fn_eager():

    exit(strategy.reduce(
        reduce_util.ReduceOp.SUM, value=per_replica_value, axis=None))

fn_graph = def_function.function(fn_eager)
# Run reduce under the strategy scope to explicitly enter
# strategy default_device scope.
with strategy.scope():
    self.assertEqual(fn_eager().numpy(), 1.0 * strategy.num_replicas_in_sync)
    self.assertEqual(fn_graph().numpy(), 1.0 * strategy.num_replicas_in_sync)

# Run reduce without a strategy scope to implicitly enter
# strategy default_device scope.
self.assertEqual(fn_eager().numpy(), 1.0 * strategy.num_replicas_in_sync)
self.assertEqual(fn_graph().numpy(), 1.0 * strategy.num_replicas_in_sync)
