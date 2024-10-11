# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    loss_scale = loss_scale_module.DynamicLossScale(
        initial_loss_scale=1, increment_period=2, multiplier=3)
    if context.executing_eagerly():
        self.assertEqual(repr(loss_scale),
                         'DynamicLossScale(current_loss_scale=1.0, '
                         'num_good_steps=0, initial_loss_scale=1.0, '
                         'increment_period=2, multiplier=3.0)')
    else:
        self.assertEqual(repr(loss_scale),
                         'DynamicLossScale(initial_loss_scale=1.0, '
                         'increment_period=2, multiplier=3.0)')
