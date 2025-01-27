# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
if strategy_test_lib.is_tpu_strategy:
    self.skipTest("b/139550827: Cannot do variable.assign in replica context "
                  "of TPUStrategy")
with distribution.scope():
    w_assign, w_apply, ema_w = distribution.run(
        self._ema_replica_fn_graph)
self.assertEqual(ema_w.name, "w/ExponentialMovingAverage:0")
self.evaluate(variables.global_variables_initializer())
self.evaluate(distribution.experimental_local_results(w_apply))
self.evaluate(distribution.experimental_local_results(w_assign))
self.evaluate(distribution.experimental_local_results(w_apply))
self.assertAllClose(
    self.evaluate(distribution.experimental_local_results(ema_w))[0],
    [0.89999998])
