# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
if (type_a is int) and (type_b is _int_tensor):
    self.skipTest('b/124378596')
a = type_a(a)
b = type_b(b)
self.assertFunctionMatchesEager(dependent_inner_while, a, b)
