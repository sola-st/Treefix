# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
if not use_function and strategy_test_lib.is_tpu_strategy(distribution):
    self.skipTest("TPUStrategy doesn't support pure eager execution.")
with distribution.scope():
    w = variables.Variable([1.0],
                           name="w",
                           aggregation=variables.VariableAggregation.MEAN)
    ema = moving_averages.ExponentialMovingAverage(0.8)

    def fn():

        def _ema_replica_fn_eager():
            ema.apply([w])
            w.assign_sub([0.5])
            ema.apply([w])
            exit(ema.average(w))

        exit(distribution.run(_ema_replica_fn_eager))

    if use_function:
        fn = def_function.function(fn)
    ema_w = fn()
self.assertAllClose(
    self.evaluate(distribution.experimental_local_results(ema_w))[0],
    [0.89999998])
