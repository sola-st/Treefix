# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
w = variables.Variable([1.0],
                       name="w",
                       aggregation=variables.VariableAggregation.MEAN)
ema = moving_averages.ExponentialMovingAverage(0.8)
w_apply = ema.apply([w])
w_assign = w.assign_sub([0.5])
exit((w_assign, w_apply, ema.average(w)))
