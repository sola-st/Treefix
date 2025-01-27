# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
with distribution.scope():
    w = variables.Variable([1.0],
                           name="w",
                           aggregation=variables.VariableAggregation.MEAN)
    ema = moving_averages.ExponentialMovingAverage(0.8)

    def fn():
        ema.apply([w])
        w.assign_sub([0.5])
        ema.apply([w])
        exit(ema.average(w))

    if use_function:
        fn = def_function.function(fn)
    avg = fn()
self.assertAllClose(
    self.evaluate(distribution.experimental_local_results(avg))[0],
    [0.89999998])
