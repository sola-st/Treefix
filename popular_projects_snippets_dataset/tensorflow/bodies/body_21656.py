# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
v0 = variables.Variable(10.0, name="v0")
v1 = variables.Variable(30.0, name="v1")
# Add a non-trainable variable.
v2 = variables.Variable(20.0, name="v2", trainable=False)
ema = moving_averages.ExponentialMovingAverage(0.25, name="foo_avg")
self.assertEqual("v0/foo_avg", ema.average_name(v0))
self.assertEqual("v1/foo_avg", ema.average_name(v1))
vars_to_restore = ema.variables_to_restore([v0, v1, v2])
self.assertAllEqual(
    sorted(vars_to_restore.keys()),
    sorted([
        ema.average_name(v0), ema.average_name(v1), ema.average_name(v2)
    ]))
ema.apply([v0, v1])
self.assertEqual(ema.average(v0).name[:-len(":0")], ema.average_name(v0))
self.assertEqual(ema.average(v1).name[:-len(":0")], ema.average_name(v1))
