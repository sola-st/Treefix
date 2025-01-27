# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
x = type_(x)
self.assertFunctionMatchesEager(target, x, a, 0)
