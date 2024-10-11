# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
var = variables.Variable([0.0, 0.0])
val = constant_op.constant([1.0, 2.0], dtypes.float32)
decay = 0.25
if context.executing_eagerly():
    self.assertAllClose([0.0, 0.0], self.evaluate(var))
    assign = moving_averages.assign_moving_average(var, val, decay)
    self.assertAllClose(
        [1.0 * (1.0 - 0.25) / (1 - 0.25), 2.0 * (1.0 - 0.25) / (1 - 0.25)],
        self.evaluate(var))
else:
    assign = moving_averages.assign_moving_average(var, val, decay)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([0.0, 0.0], self.evaluate(var))
    assign.op.run()
    self.assertAllClose(
        [1.0 * (1.0 - 0.25) / (1 - 0.25), 2.0 * (1.0 - 0.25) / (1 - 0.25)],
        self.evaluate(var))
