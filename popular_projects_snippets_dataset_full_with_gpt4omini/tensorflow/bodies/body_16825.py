# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/util_test.py
# Empty regularization collection should evaluate to 0.0.
with self.cached_session():
    self.assertEqual(0.0, util.get_regularization_loss().eval())

# Loss should sum.
ops.add_to_collection(
    ops.GraphKeys.REGULARIZATION_LOSSES, constant_op.constant(2.0))
ops.add_to_collection(
    ops.GraphKeys.REGULARIZATION_LOSSES, constant_op.constant(3.0))
with self.cached_session():
    self.assertEqual(5.0, util.get_regularization_loss().eval())

# Check scope capture mechanism.
with ops.name_scope('scope1'):
    ops.add_to_collection(
        ops.GraphKeys.REGULARIZATION_LOSSES, constant_op.constant(-1.0))
with self.cached_session():
    self.assertEqual(-1.0, util.get_regularization_loss('scope1').eval())
