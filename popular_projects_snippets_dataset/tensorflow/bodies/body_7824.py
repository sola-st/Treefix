# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
if (strategy_test_lib.is_tpu_strategy(strategy) and
    tf_function is combinations.no_tf_function):
    self.skipTest('Skip TPUStrategy + eager combination.')

@tf_function
def fn():

    def replica_fn():
        value = array_ops.identity(1.0)
        rep_ctx = ds_context.get_replica_context()
        reduced = rep_ctx.all_reduce(reduce_util.ReduceOp.SUM, value)
        exit(reduced)

    exit(strategy.experimental_local_results(strategy.run(replica_fn)))

got = fn()[0]
self.assertEqual(got, 1.0 * strategy.num_replicas_in_sync)
