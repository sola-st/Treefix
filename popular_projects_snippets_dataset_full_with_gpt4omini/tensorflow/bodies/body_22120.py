# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    loss_scale = loss_scale_module.DynamicLossScale()
    grad = constant_op.constant(4.0)
    _, should_apply = loss_scale.update(grad)
    self.assertTrue(self.evaluate(should_apply))
