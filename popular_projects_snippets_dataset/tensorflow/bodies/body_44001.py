# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
x = type_(x)
self.assertFunctionMatchesEager(dependent_imbalanced_inner_if, x)
