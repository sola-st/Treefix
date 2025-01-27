# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
if n == 0 and type_ is tf.constant:
    self.skipTest("TF loop must initialize y['a']")

n = type_(n)
self.assertFunctionMatchesEager(for_imbalanced, n, 0)
