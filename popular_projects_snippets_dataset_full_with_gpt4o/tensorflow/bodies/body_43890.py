# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
a = type_(a)
with self.assertRaisesRegex(exc_type, exc_regex):
    tf.function(target)(a)
