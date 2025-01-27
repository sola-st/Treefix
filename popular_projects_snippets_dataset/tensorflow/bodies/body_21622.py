# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
var = variables.Variable([10.0, 11.0])
val = constant_op.constant([1.0, 2.0], dtypes.float32)
decay = 0.25
if context.executing_eagerly():
    self.assertAllClose([10.0, 11.0], self.evaluate(var))
    assign = moving_averages.assign_moving_average(
        var, val, decay, zero_debias=False)
    self.assertAllClose(
        [10.0 * 0.25 + 1.0 * (1.0 - 0.25), 11.0 * 0.25 + 2.0 * (1.0 - 0.25)],
        self.evaluate(var))
else:
    assign = moving_averages.assign_moving_average(
        var, val, decay, zero_debias=False)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([10.0, 11.0], self.evaluate(var))
    assign.op.run()
    self.assertAllClose(
        [10.0 * 0.25 + 1.0 * (1.0 - 0.25), 11.0 * 0.25 + 2.0 * (1.0 - 0.25)],
        self.evaluate(var))
