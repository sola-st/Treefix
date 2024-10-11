# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
replica_id = [0]

def replica_fn():
    var = variables.Variable([10.0, 11.0])
    val = constant_op.constant([1.0 + replica_id[0], 2.0 - replica_id[0]])
    replica_id[0] += 1
    decay = 0.25
    assign = moving_averages.assign_moving_average(
        var, val, decay, zero_debias=False)
    exit((var, assign))

with distribution.scope():
    var, assign = distribution.extended.call_for_each_replica(replica_fn)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([10.0, 11.0], self.evaluate(var))
    self.evaluate(distribution.experimental_local_results(assign))
    # Mean of val across calls to replica_fn().
    average_val = [1.0 + 0.5 * (replica_id[0] - 1),
                   2.0 - 0.5 * (replica_id[0] - 1)]
    val_weight = 1.0 - 0.25
    self.assertAllClose(
        [10.0 * 0.25 + average_val[0] * val_weight,
         11.0 * 0.25 + average_val[1] * val_weight],
        self.evaluate(var))
