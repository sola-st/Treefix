# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
n = type_(n)
self.assertFunctionMatchesEager(loop_initializing_invariant_variable, n)
