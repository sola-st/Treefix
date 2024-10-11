# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
ema = moving_averages.ExponentialMovingAverage(0.25, name="foo_avg")
v = variables.Variable(_Repeat(10.0, 2), name="v")
self.assertIsNone(xla_sharding.get_tensor_sharding(v))
v = xla_sharding.mesh_split(v, np.array([0, 1]), [0], use_sharding_op=False)
self.assertIsNotNone(xla_sharding.get_tensor_sharding(v))
self.evaluate(variables.global_variables_initializer())
ema.apply([v])
avg = ema.average(v)
self.assertEqual(
    xla_sharding.get_tensor_sharding(v),
    xla_sharding.get_tensor_sharding(avg))
