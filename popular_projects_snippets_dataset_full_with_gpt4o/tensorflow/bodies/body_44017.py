# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
with self.assertRaisesRegex(ValueError, 'must be defined before the loop'):
    tf.function(loop_initializing_variant_variable)(tf.constant(n))
