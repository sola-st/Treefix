# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
with distribution.scope():
    var = variables.Variable([10.0, 11.0])
    val = constant_op.constant([1.0, 2.0])
    decay = 0.25
    # NOTE(josh11b): We currently generate an error if val is a PerReplica
    # value.
    assign = moving_averages.assign_moving_average(
        var, val, decay, zero_debias=False)

    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([10.0, 11.0], self.evaluate(var))
    self.evaluate(assign)
    average_val = [1.0, 2.0]
    val_weight = 1.0 - 0.25
    self.assertAllClose(
        [10.0 * 0.25 + average_val[0] * val_weight,
         11.0 * 0.25 + average_val[1] * val_weight],
        self.evaluate(var))
    # Also try assign.op.
    self.evaluate(assign.op)
    orig_weight = 0.25 * 0.25
    val_weight = 1.0 - orig_weight
    self.assertAllClose(
        [10.0 * orig_weight + average_val[0] * val_weight,
         11.0 * orig_weight + average_val[1] * val_weight],
        self.evaluate(var))
