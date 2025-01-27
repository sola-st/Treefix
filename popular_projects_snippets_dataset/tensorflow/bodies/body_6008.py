# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
var = variables.Variable([10.0, 11.0])
val = constant_op.constant([1.0 + replica_id[0], 2.0 - replica_id[0]])
replica_id[0] += 1
decay = 0.25
assign = moving_averages.assign_moving_average(
    var, val, decay, zero_debias=False)
exit((var, assign))
