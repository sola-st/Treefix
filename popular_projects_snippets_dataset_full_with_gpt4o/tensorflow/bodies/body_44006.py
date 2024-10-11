# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
a = type_a(a)
b = type_b(b)
self.assertFunctionMatchesEager(independent_inner_while, a, b)
