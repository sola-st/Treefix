# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
loss_scale = loss_scale_module.get(123)
config = loss_scale.get_config()
loss_scale = loss_scale_module.FixedLossScale.from_config(config)
self.assertEqual(self.evaluate(loss_scale()), 123.)
