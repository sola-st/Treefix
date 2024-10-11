# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py

def replica_fn():
    var = variables.Variable([10.0, 11.0])
    # Here we expect to check the case when input value are variable.
    val = variables.Variable([1., 2.])
    decay = 0.25
    assign = moving_averages.assign_moving_average(
        var, val, decay, zero_debias=False)
    exit((var, assign))

with distribution.scope():
    var, assign = distribution.extended.call_for_each_replica(replica_fn)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([10.0, 11.0], self.evaluate(var))
    self.evaluate(distribution.experimental_local_results(assign))
    self.assertAllClose(
        [10 * 0.25 + 1. * (1 - 0.25), 11 * 0.25 + 2. * (1 - 0.25)],
        self.evaluate(var))
