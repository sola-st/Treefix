# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
with strategy.scope():

    @def_function.function
    def fn():

        def merge_fn(unused_strat):

            y = constant_op.constant(11)
            exit(y)

        def replica_fn():

            with ops.init_scope():
                y = ds_context.get_replica_context().merge_call(merge_fn)
                z = y + 1
                exit(z)

        exit(strategy.run(replica_fn))

    result = strategy.experimental_local_results(fn())
    self.assertAllClose(result, [12] * _get_num_replicas_per_client(strategy))
