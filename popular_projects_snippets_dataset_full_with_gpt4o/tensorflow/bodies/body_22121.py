# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
loss_scale = loss_scale_module.DynamicLossScale(
    initial_loss_scale=1, increment_period=2, multiplier=3)
config = loss_scale.get_config()
loss_scale = loss_scale_module.DynamicLossScale.from_config(config)
self.evaluate(variables.global_variables_initializer())
self.assertEqual(self.evaluate(loss_scale()), 1)
self.assertEqual(loss_scale.increment_period, 2)
self.assertEqual(loss_scale.multiplier, 3)
