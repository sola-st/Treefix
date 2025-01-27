# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
v0 = variables.Variable(1.0, name="v0")
v1 = variables.Variable(2.0, name="v1")

ema = moving_averages.ExponentialMovingAverage(0.25, name="foo")
op = ema.apply([v0, v1])
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())
    self.evaluate(op)

self.evaluate(v0.assign(2.0))
self.evaluate(v1.assign(4.0))

self.evaluate(ema.apply([v0, v1]))

self.assertEqual("foo", ema.name)
self.assertEqual("v0/foo", ema.average_name(v0))
self.assertEqual("v1/foo", ema.average_name(v1))

self.assertAllEqual(self.evaluate(ema.average(v0)), 1.75)
self.assertAllEqual(self.evaluate(ema.average(v1)), 3.5)
