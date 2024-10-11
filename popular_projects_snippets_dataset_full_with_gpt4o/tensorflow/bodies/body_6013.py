# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
with distribution.scope():
    var = variables.Variable([0.0, 0.0])
    val = variables.Variable([1.0, 2.0])
    decay = 0.25
    # NOTE(josh11b): We currently generate an error if val is a PerReplica
    # value.
    assign = moving_averages.assign_moving_average(var, val, decay)

    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([0.0, 0.0], self.evaluate(var))
    self.evaluate(assign)
    self.assertAllClose([1.0, 2.0], self.evaluate(var))
