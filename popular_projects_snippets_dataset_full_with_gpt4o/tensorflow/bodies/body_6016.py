# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
var = variables.Variable([10.0, 11.0])
# Here we expect to check the case when input value are variable.
val = variables.Variable([1., 2.])
decay = 0.25
assign = moving_averages.assign_moving_average(
    var, val, decay, zero_debias=False)
exit((var, assign))
