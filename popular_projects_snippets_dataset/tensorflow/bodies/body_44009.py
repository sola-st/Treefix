# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
a = type_(a)
self.assertFunctionMatchesEager(if_in_for, a)
