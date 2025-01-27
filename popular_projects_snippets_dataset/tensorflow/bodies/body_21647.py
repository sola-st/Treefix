# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
v0 = variables.Variable(0, name="v0")
add_to_v0 = v0.assign_add(1)
v1 = variables.Variable([10.0], name="v1")
assign_to_v1 = v1.assign([20.0])
ema = moving_averages.ExponentialMovingAverage(0.25)
with ops.control_dependencies([add_to_v0]):
    ema_op = ema.apply([v1])
# the moving average of v1 should not have any control inputs
v1_avg = ema.average(v1)
self.assertEqual([], v1_avg.initializer.control_inputs)
self.assertEqual([], v1_avg.value().op.control_inputs)
self.assertEqual([], v1_avg.value().op.control_inputs)
# We should be able to initialize v1_avg before v0.
self.evaluate(v1_avg.initializer)
self.evaluate(v0.initializer)
self.assertEqual([10.0], self.evaluate(v1_avg))
# running ema_op should add to v0 (in addition to updating v1_avg)
self.evaluate(assign_to_v1)
self.evaluate(ema_op)
self.assertEqual(1, self.evaluate(v0))
self.assertEqual([17.5], self.evaluate(v1_avg))
