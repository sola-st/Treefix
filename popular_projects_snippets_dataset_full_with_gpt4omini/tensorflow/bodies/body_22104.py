# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
loss_scale = loss_scale_module.FixedLossScale(123)
self.assertEqual(repr(loss_scale), 'FixedLossScale(123.0)')
