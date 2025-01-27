# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
if b == 11 and type_ is tf.constant:
    self.skipTest("TF loop must initialize y['a']")

b = type_(b)
self.assertFunctionMatchesEager(while_imbalanced, b)
