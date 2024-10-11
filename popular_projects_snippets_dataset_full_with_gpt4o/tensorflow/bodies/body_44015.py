# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
with self.assertRaises(UnboundLocalError):
    tf.function(loop_initializing_invariant_variable)(0)
with self.assertRaisesRegex(
    tf.errors.InvalidArgumentError, 'loop must iterate at least once'):
    tf.function(loop_initializing_invariant_variable)(tf.constant(0))
