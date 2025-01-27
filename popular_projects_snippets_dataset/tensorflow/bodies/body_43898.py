# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
with self.assertRaisesRegex(
    tf.errors.InvalidArgumentError,
    r"loop must iterate at least once to initialize y\[\\'a\\'\]"):
    tf.function(for_imbalanced)(tf.constant(0), 0)
