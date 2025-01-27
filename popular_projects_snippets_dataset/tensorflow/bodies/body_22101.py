# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
loss_scale_value = 1000
loss_scale = loss_scale_module.FixedLossScale(loss_scale_value)

update_op, should_apply = loss_scale.update([constant_op.constant(0.)])
self.evaluate(update_op)
# should_apply should be a bool instead of a tensor, so that a tf.cond does
# not have to be built in the graph by the caller.
self.assertIsInstance(should_apply, bool)
self.assertTrue(should_apply)
self.assertEqual(loss_scale_value, self.evaluate(loss_scale()))

update_op, should_apply = loss_scale.update(
    [constant_op.constant(float('NaN'))])
self.evaluate(update_op)
self.assertIsInstance(should_apply, bool)
self.assertTrue(should_apply)
self.assertEqual(loss_scale_value, self.evaluate(loss_scale()))
