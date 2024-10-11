# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
scalar = loss_scale_module.get('dynamic')
scalar2 = loss_scale_module.DynamicLossScale()
self.assertEqual(scalar.initial_loss_scale, scalar2.initial_loss_scale)
self.assertEqual(scalar.increment_period, scalar2.increment_period)
self.assertEqual(scalar.multiplier, scalar2.multiplier)
